django-adminfilters
===================

A collection of FieldListFilters for object list filtering in the
django administrator.

Multiple selection filters allow filtering on one or more filter values.
The following multiple selection filters are available:
 - UnionFieldListFilter: filters results matching ANY of the filter
   values. Similar to the Union operation on sets.
 - IntersectionFieldListFilter: filters results maching ALL of the
   filter values. Similar to the Intersection operation on sets.

How to use
==========

Import the filter and add it as a FieldListFilter implementation to the
list_filter attribute of a ModelAdmin as described in the `Django Documentation <https://docs.djangoproject.com/en/1.4/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter>`_.

::
    from extraadminfilters.filters import UnionFieldListFilter

    class CountryAdmin(admin.ModelAdmin):
        list_filter = (
            ('continent', UnionFieldListFilter),
            'languages'
        )
