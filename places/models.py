from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.CharField('Краткое описание', max_length=500)
    description_long = HTMLField('Полное описание', max_length=5000)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Картинка', null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место', related_name='images')
    position = models.PositiveIntegerField('Позиция', default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} - {self.place.title}'
