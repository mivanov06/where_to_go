from django.contrib import admin

from places.models import Place, Image


# Register your models here.

@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'position')