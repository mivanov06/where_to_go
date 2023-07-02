from django.contrib import admin

from places.models import Place


# Register your models here.

@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('title',)