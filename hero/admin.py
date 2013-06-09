from django.contrib import admin
from hero.models import Hero, Rank


class HeroAdmin(admin.ModelAdmin):
    pass

class RankAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hero, HeroAdmin)
admin.site.register(Rank, RankAdmin)