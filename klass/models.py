from django.db import models
from django.utils.text import slugify


class Klass(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=5)

    def __unicode__(self):
        return unicode(self.name)

    def slug(self):
        return slugify(self.name)