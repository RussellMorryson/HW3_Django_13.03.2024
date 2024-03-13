from django.core.management.base import BaseCommand
from myapp.models import User, Product, Order

class Command(BaseCommand):
    help = "Create order."  
    
    def handle(self, *args, **kwargs):
        order = Order.objects.create(customer = User.objects.filter(pk=1).first(), 
                                     total_price = Product.objects.filter(pk=2).first().price)
        product = Product.objects.filter(pk=1)
        order.products.set(product)
        order.save()
        self.stdout.write(f'{order}')