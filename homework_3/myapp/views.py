from django.shortcuts import render

# Create your views here.
import logging
from myapp.models import User, Product, Order
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return render(request, "myapp/index.html")

def dateValue(first:str, second:str) -> bool:
    #first 2024-03-13 12:50:44.677859+00:00
    #second 2024-03-12 12:54:09.253827

    #calendar = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    f_year = int(first[0] + first[1]+ first[2]+ first[3])
    s_year = int(second[0] + second[1]+ second[2]+ second[3])

    f_month = int(first[5] + first[6])
    s_month = int(second[5] + second[6])

    f_day = int(first[8] + first[9])
    s_day = int(second[8] + second[9])

    f_res = f_year * 365 + f_month*30 + f_day
    s_res = s_year * 365 + s_month*30 + s_day

    if f_res >= s_res: return True
    else: return False

def last_week(request):
    date = datetime.today() - timedelta(days=7)
    logger.info(f'The period from {str(date)}')
    context = {}
    orders = {}
    for obj in Order.objects.all():
        if (dateValue(str(obj.date_ordered), str(date))):
            orders[obj.pk] = f'{obj}'
    context['orders'] = orders
    return render(request, "myapp/index.html", context)

def last_month(request):
    date = datetime.today() - timedelta(days=30)
    logger.info(f'The period from {str(date)}')
    context = {}
    orders = {}
    for obj in Order.objects.all():
        if (dateValue(str(obj.date_ordered), str(date))):
            orders[obj.pk] = f'{obj}'
    
    context['orders'] = orders
    return render(request, "myapp/index.html", context)

def last_year(request):
    date = datetime.today() - timedelta(days=365)
    logger.info(f'The period from {str(date)}')
    context = {}
    orders = {}
    for obj in Order.objects.all():
        if (dateValue(str(obj.date_ordered), str(date))):
            orders[obj.pk] = f'{obj}'

    context['orders'] = orders
    return render(request, "myapp/index.html", context)

def about(request):
    logger.info('About page accessed')
    return render(request, "myapp/about.html")

