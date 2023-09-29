import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    help = 'Imports phones data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                phone = Phone(
                    name=row[0],
                    price=float(row[1]),
                    image=row[2],
                    release_date=row[3],
                    lte_exists=bool(row[4])
                )
                phone.save()
        self.stdout.write(self.style.SUCCESS('Phones imported successfully!'))