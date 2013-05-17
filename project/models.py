from django.db import models


class Continent(models.Model):

    description = models.CharField(max_length=255, blank=False)

    def __unicode__(self):
        return self.description


class Language(models.Model):

    description = models.CharField(max_length=255, blank=False)

    def __unicode__(self):
        return self.description


class Country(models.Model):

    description = models.CharField(max_length=255, blank=False)
    continent = models.ForeignKey(Continent, db_index=True)
    languages = models.ManyToManyField(Language)

    def __unicode__(self):
        return self.description
