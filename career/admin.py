from django.contrib import admin
from career.models import Career

class CareerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Career, CareerAdmin)