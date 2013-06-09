from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Career(models.Model):
    name = models.CharField(max_length=100)
    region = models.SmallIntegerField(choices=settings.REGIONS)

    last_api_request = models.DateTimeField()

    @property
    # returns the slug of this career, ex. aveley-2218
    def slug(self):
        # slugify deletes the # in a battletag, replace it by a dash
        return slugify(self.name.replace('#', '-'))

    def fill_from_json(self, json):
        self.name = 'test'
        self.region = settings.EUROPE

        self.save()
