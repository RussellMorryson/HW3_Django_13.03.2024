from django.core.management.base import BaseCommand
from myapp.models import User, Product, Order
from myapp.views import dateValue
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Get last week orders."
    
    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='User age')
    
    def handle(self, *args, **kwargs):
        date = datetime.today() - timedelta(days=365)
        orders = []
        for obj in Order.objects.all():
           if (dateValue(str(obj.date_ordered), str(date))):
                orders.append(obj)

        # for obj in orders:
        #     if obj.customer != User.objects.filter(pk=1).first():
        #         orders.remove(obj)

        for obj in orders:
            print(f'Customer: {obj.customer}, product: {obj.products}, date ordered: {obj.date_ordered}, total price: {obj.total_price}.')