from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.filters import FieldListFilter
from django.contrib.admin.filters import RelatedFieldListFilter
from django.contrib.admin.util import get_model_from_relation
from django.utils.encoding import smart_text


class MultipleSelectionFieldListFilter(FieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        other_model = get_model_from_relation(field)
        if hasattr(field, 'rel'):
            rel_name = field.rel.get_related_field().name
        else:
            rel_name = other_model._meta.pk.name
        self.lookup_kwarg = '%s__%s__in' % (field_path, rel_name)
        self.lookup_kwarg_isnull = '%s__isnull' % field_path
        self.lookup_val = request.GET.get(self.lookup_kwarg, None)
        self.lookup_val_isnull = request.GET.get(self.lookup_kwarg_isnull, None)
        self.lookup_choices = field.get_choices(include_blank=False)
        super(MultipleSelectionFieldListFilter, self).__init__(field, request, params, model, model_admin, field_path)
        if hasattr(field, 'verbose_name'):
            self.lookup_title = field.verbose_name
        else:
            self.lookup_title = other_model._meta.verbose_name
        self.title = self.lookup_title

    def has_output(self):
        if (isinstance(self.field, models.related.RelatedObject)
                and self.field.field.null or hasattr(self.field, 'rel')
                    and self.field.null):
            extra = 1
        else:
            extra = 0
        return len(self.lookup_choices) + extra > 1

    def expected_parameters(self):
        return [self.lookup_kwarg, self.lookup_kwarg_isnull]

    def choices(self, cl):

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


def multiple_selection_field_list_filter_test(f):
    if hasattr(f, 'rel') and (bool(f.rel) or isinstance(f, models.related.RelatedObject)):
        if hasattr(f.model, 'multiple_selection_fields') and f.name in f.model.multiple_selection_fields():
            return True
    return False

MultipleSelectionFieldListFilter.register(
    multiple_selection_field_list_filter_test,
    MultipleSelectionFieldListFilter,
    True)
