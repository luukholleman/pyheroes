from django.db import models
from pyheroes import settings


class Task(models.Model):
    HERO = 1
    CAREER = 2
    ITEM = 3

    TASKS = (
        (HERO, 'Hero'),
        (CAREER, 'Career'),
        (ITEM, 'Item'),
    )

    type = models.SmallIntegerField(choices=TASKS)
    region = models.SmallIntegerField(choices=settings.REGIONS)
    battletag = models.CharField(max_length=50)
    hero_id = models.IntegerField()
    item_id = models.CharField(max_length=200)
    started = models.BooleanField()
    ended = models.BooleanField()

    @property
    def battletag_slug(self):
        return self.battletag.replace('#', '-')