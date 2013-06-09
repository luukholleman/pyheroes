from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    sequence = models.SmallIntegerField()

    def __unicode__(self):
        return unicode(self.name)

class Ranklist(models.Model):
    category = models.ForeignKey(Category)

    name = models.CharField(max_length=20)
    stat = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.name)
