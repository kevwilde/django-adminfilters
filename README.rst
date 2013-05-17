What it is
==========

Optionally add multiple selection filters for FK and m2m fields in Django admin changeview.

How to use
==========

- import "project/filter.py" once
- add the attribute multiple_selection_list_filter to your ModelAdmin
  to specify which filters require multiple selection

Example::

    class CountryAdmin(admin.ModelAdmin):
        ...
        list_filter = ['continent', 'languages', ]
        multiple_selection_list_filter = ['continent', 'languages', ]

Implementation details
======================

A new filter MultipleSelectionFieldListFilter is registered instead of RelatedFieldListFilter,
and provides multiple selection or fallback to single selection behaviour according to
ModelAdmin prescriptions.

Todo
====

- move functionality into separate installable app
- in the meantime, just copy "product/filters.py" somewhere and include it once
