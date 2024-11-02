import csv
from django.core.management.base import BaseCommand
from app_condo.models import District, Subdistrict, NearestRoad

class Command(BaseCommand):
    help = 'Import data from CSV'

    def handle(self, *args, **kwargs):
        # Use a relative path from the management command location
        csv_file_path = 'app_condo/data/condo_data_final.csv'  # Adjust path as needed
        
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Get or create district
                    district, created = District.objects.get_or_create(
                        name=row['District']
                    )
                    
                    # Get or create subdistrict
                    subdistrict, created = Subdistrict.objects.get_or_create(
                        name=row['Subdistrict'],
                        district=district
                    )
                    
                    # Get or create nearest road
                    nearest_road, created = NearestRoad.objects.get_or_create(
                        name=row['NearestRoad'],
                        subdistrict=subdistrict
                    )
            
            self.stdout.write(
                self.style.SUCCESS('Data imported successfully')
            )
            
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'Could not find file: {csv_file_path}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error importing data: {str(e)}')
            )