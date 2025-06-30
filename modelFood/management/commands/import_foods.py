import csv
from django.core.management.base import BaseCommand
from modelFood.models import Food  # change if your app name is different

class Command(BaseCommand):
    help = 'Import foods from foods.csv'

    def handle(self, *args, **kwargs):
        with open('foods.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Food.objects.create(
                    name=row['name'],
                    description=row['description'],
                    category=row['category'],
                    price=row['price'],
                    calories=row['calories'] or None,
                    protein=row['protein'] or None,
                    fat=row['fat'] or None,
                    carbohydrates=row['carbohydrates'] or None,
                    image=row['image']
                )
        self.stdout.write(self.style.SUCCESS('Foods imported successfully!'))