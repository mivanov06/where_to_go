from django.contrib import admin

from places.image_preview import image_preview
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = [image_preview]


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'position')
    readonly_fields = [image_preview]
