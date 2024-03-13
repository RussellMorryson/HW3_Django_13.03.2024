from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):
    help = "Create product."  
    
    def handle(self, *args, **kwargs):
        product = Product(name='Bionicle', price=15000.0, description='Baraka')
        product.save()
        self.stdout.write(f'{product}')
