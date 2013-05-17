
What it is
==========

Optionally add multiple selection filters for FK and m2m fields in Django admin changeview.

How to use
==========

- import "project/filter.py" once
- add a classmethod multiple_selection_fields() to your Model which returns
  the list of fields to be filtererd using multiple selection in;


Example::

    class Country(models.Model):

        description = models.CharField(max_length=255, blank=False)
        continent = models.ForeignKey(Continent, db_index=True)
        languages = models.ManyToManyField(Language)

        def __unicode__(self):
            return self.description

        @classmethod
        def multiple_selection_fields(self):
            return ['continent', 'languages', ]

Todo
====

- move functionality into separate installable app
- move multiple selectable field list in ModelsAdmin
  (requires a small addition to django.contrib.admin.filters or some refactoring)
