import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загрузка данных о месте в базу данных'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_url', type=str, help='Ссылка на данные с местом на карте'
        )

    def get_place(self, content):
        place, _ = Place.objects.update_or_create(
            title=content['title'],
            description_short=content.get('description_short', ''),
            description_long=content.get('description_long', ''),
            longitude=content['coordinates']['lng'],
            latitude=content['coordinates']['lat']
        )
        return place

    def get_images(self, content, place):
        images_url = content.get('imgs', [])
        for index, image_url in enumerate(images_url, 1):
            image_name = image_url.split('/')[-1]
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image = ContentFile(
                image_response.content,
                name=image_name
            )
            image, _ = Image.objects.update_or_create(
                place=place,
                image=image,
                position=index,
            )

    def handle(self, *args, **kwargs):
        file_url = kwargs['file_url']
        response = requests.get(file_url)
        response.raise_for_status()
        content = response.json()
        place = self.get_place(content)
        self.get_images(content, place)
