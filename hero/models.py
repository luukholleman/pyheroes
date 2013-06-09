from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from career.models import Career
from klass.models import Klass
from ranklist.models import Ranklist
from django.core.cache import cache


class Hero(models.Model):
    MALE = 0
    FEMALE = 1

    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    BARBARIAN = 1
    DEMON_HUNTER = 2
    MONK = 3
    WITCH_DOCTOR = 4
    WIZARD = 5

    career = models.ForeignKey(Career)

    blizzard_id = models.IntegerField()
    name = models.CharField(max_length=100)
    hardcore = models.BooleanField()
    level = models.IntegerField()
    paragon_level = models.IntegerField()
    gender = models.SmallIntegerField(choices=GENDERS)
    klass = models.ForeignKey(Klass)
    last_played = models.DateTimeField()
    region = models.SmallIntegerField(choices=settings.REGIONS)
    last_api_request = models.DateTimeField()

    ranklist = None

    class Meta:
        verbose_name_plural = 'Heroes'

    def __unicode__(self):
        return unicode(self.name + ' - ' + self.career.name + ' - ' + self.get_region_display())

    def __getattr__(self, item):
        # stats of this hero are not stored in the model, we need to query them from another table
        if item in settings.RANKLISTS:
            return self.get_ranklist_value(item)

        return super(Hero, self).__getattr__(item)

    @property
    def icon(self):
        return 'img/class-icons/witch-doctor_male.png'

    @property
    def url(self):
        return reverse('hero.detail', args=(self.id, self.career.slug, self.blizzard_id))

    @property
    #returns the mode of this hero as string, Softcore or Hardcore
    def mode(self):
        if self.hardcore:
            return 'Hardcore'

        return 'Softcore'

    @property
    #returns the mode of this hero as slug, softcore or hardcore
    def mode_slug(self):
        return slugify(self.mode)

    @property
    # returns the absolute url to the battle net page of this hero
    def battle_net_url(self):
        return 'http://%s.battle.net/d3/en/profile/%s/hero/%s' % ('eu', hero.ca)

    # get the hero's rank in a stat ranklist
    def get_ranklist_value(self, stat):
        # return 0 if this hero does not meet minimum rank level
        if self.level < settings.MINIMUM_RANK_LEVEL:
            return 0



        # try to get the rank, set rank to 0 if one of the necessary records could not be found
        try:
            rank = self.get_ranklist_record(stat).value
        except Ranklist.DoesNotExist:
            rank = 0
        except Rank.DoesNotExist:
            rank = 0

        # update cache for next time
        cache.set('hero.test', rank)

        return rank

    def get_ranklist_record(self, stat):
        caching_name = 'hero.rankrecord.' + stat

        if cache.get(caching_name):
            return cache.get(caching_name)

        ranklist = Ranklist.objects.get(stat=stat)

        rank_record = self.rank_set.get(ranklist=ranklist)

        cache.set(caching_name, rank_record)

        return rank_record

class Rank(models.Model):
    hero = models.ForeignKey(Hero)
    ranklist = models.ForeignKey(Ranklist)

    value = models.IntegerField()
    all_all = models.IntegerField()
    all_class = models.IntegerField()
    region_all = models.IntegerField()
    region_class = models.IntegerField()
