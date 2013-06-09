from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from ranklist.models import Ranklist, Category


class RanklistCategoryAdmin(ModelAdmin):
    pass

class RanklistAdmin(ModelAdmin):
    pass

admin.site.register(Category, RanklistCategoryAdmin)
admin.site.register(Ranklist, RanklistAdmin)