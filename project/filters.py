from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.filters import FieldListFilter
from django.contrib.admin.filters import RelatedFieldListFilter
from django.contrib.admin.util import get_model_from_relation
from django.utils.encoding import smart_text


class MultipleSelectionFieldListFilter(RelatedFieldListFilter):

    def __init__(self, field, request, params, model, model_admin, field_path):
        super(MultipleSelectionFieldListFilter, self).__init__(field, request, params, model, model_admin, field_path)
        if self.use_multiple_selection(model_admin):
            # eventually use model__field__in lookup arg to support multiple selections
            other_model = get_model_from_relation(field)
            if hasattr(field, 'rel'):
                rel_name = field.rel.get_related_field().name
            else:
                rel_name = other_model._meta.pk.name
            self.lookup_kwarg = '%s__%s__in' % (field_path, rel_name)
            self.lookup_kwarg_isnull = '%s__isnull' % field_path
            self.lookup_val = request.GET.get(self.lookup_kwarg, None)
            self.lookup_val_isnull = request.GET.get(self.lookup_kwarg_isnull, None)

    def use_multiple_selection(self, model_admin):
        fieldname = self.field.name
        if hasattr(model_admin, 'multiple_selection_list_filter') and fieldname in model_admin.multiple_selection_list_filter:
            return True
        return False

    def choices(self, cl):
        if self.use_multiple_selection(cl.model_admin):
            return self.multiple_selection_choices(cl)
        # RelatedFieldListFilter fallback
        return super(MultipleSelectionFieldListFilter, self).choices(cl)

    def multiple_selection_choices(self, cl):

        from django.contrib.admin.views.main import EMPTY_CHANGELIST_VALUE

        yield {
            'selected': self.lookup_val is None and not self.lookup_val_isnull,
            'query_string': cl.get_query_string({},
                [self.lookup_kwarg, self.lookup_kwarg_isnull]),
            'display': _('All'),
        }
        for pk_val, val in self.lookup_choices:
            # collect selected pks from query params
            pks = self.lookup_val.split(',') if self.lookup_val else []
            pk = smart_text(pk_val)
            selected = False
            if pk in pks:
                selected = True
                # remove this key from selection
                pks = [p for p in pks if p != pk]
            else:
                # add this key to selection
                pks.append(pk)
            if len(pks) <= 0:
                query_string = cl.get_query_string({}, [self.lookup_kwarg, self.lookup_kwarg_isnull])
            else:
                query_string = cl.get_query_string({self.lookup_kwarg: ','.join(pks), }, [self.lookup_kwarg_isnull])
            yield {
                'selected': selected,
                'query_string': query_string,
                'display': val,
            }
        # TODO: untested
        if (isinstance(self.field, models.related.RelatedObject)
                and self.field.field.null or hasattr(self.field, 'rel')
                    and self.field.null):
            yield {
                'selected': bool(self.lookup_val_isnull),
                'query_string': cl.get_query_string({
                    self.lookup_kwarg_isnull: 'True',
                }, [self.lookup_kwarg]),
                'display': EMPTY_CHANGELIST_VALUE,
            }


FieldListFilter.register(lambda f: (
        hasattr(f, 'rel') and bool(f.rel) or
        isinstance(f, models.related.RelatedObject)), MultipleSelectionFieldListFilter,
        True)
