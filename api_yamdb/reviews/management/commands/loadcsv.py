import csv

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

PATH_TO_UPLOAD = 'static/data/'

FILES = [
    ('category.csv', Category),
    ('genre.csv', Genre),
    ('users.csv', User),
    ('titles.csv', Title),
    ('review.csv', Review),
    ('comments.csv', Comment),
]


class Command(BaseCommand):
    help = 'Наполняет базу данными из csv'

    def handle(self, *args, **kwargs):
        for file_name, model in FILES:
            try:
                with open(
                        (PATH_TO_UPLOAD + file_name),
                        encoding='utf8'
                ) as file:
                    reader = csv.DictReader(file)
                    model.objects.all().delete()
                    for row in reader:
                        updated_row = {}
                        for field_name, value in row.items():
                            if field_name == 'category':
                                value = get_object_or_404(Category, id=value)
                            elif field_name == 'author':
                                value = get_object_or_404(User, id=value)
                            updated_row[field_name] = value
                        model.objects.get_or_create(**updated_row)
                    print(file_name + ' Успешно загружено')
            except Exception:
                print(file_name + ' Сбой загрузки')
