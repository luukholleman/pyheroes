from django.contrib import admin
from klass.models import Klass

class KlassAdmin(admin.ModelAdmin):
    pass

admin.site.register(Klass, KlassAdmin)