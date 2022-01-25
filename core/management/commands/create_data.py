import datetime
import random
from django.core.management.base import BaseCommand
from core.models import Realestate, Categories, Realtor


categories = [
    'house_to_rent',
    'house_for_sale',
    'one_bedroom',
    'two_bedroom',
    'three_bedroom'
 ]

realtor = [
    'Antony', 'James', 'Rebecca', 'Sally', 'Joe', 'Dude', 'Guy', 'Barbara'
]


def generate_realtor_name():
    index = random.randint(0, 7)
    return realtor[index]


def generate_category_name():
    index = random.randint(0, 4)
    return categories[index]


def generate_view_count():
    return random.randint(0, 100)


def generate_is_reviewed():
    val = random.randint(0, 1)
    if val == 0:
        return False
    return True


def generate_publish_date():
    year = random.randint(2000, 2030)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', type=str, help='The txt file that contains the Properties titles.')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                title = row
                realtor_name = generate_realtor_name()
                category_name = generate_category_name()
                publish_date = generate_publish_date()
                views = generate_view_count()
                reviewed = generate_is_reviewed()

                realtor_name = Realtor.objects.get_or_create(
                    name=realtor_name
                )

                property = Realestate(
                    title=title,
                    realtor=Realtor.objects.get(name=realtor_name),
                    publish_date=publish_date,
                    views=views,
                    reviewed=reviewed
                )

                property.save()

                realestate = Realestate.objects.get_or_create(name=category_name)

                property.categories.add(
                    Realestate.objects.get(name=category_name))

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
