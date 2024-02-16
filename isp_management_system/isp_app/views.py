from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Customer

def activate_user_view(request, ip_address):
    customer = get_object_or_404(Customer, ip_address=ip_address)
    customer.subscription_status = True
    customer.save()
    return HttpResponse(status=200)

def deactivate_user_view(request, ip_address):
    customer = get_object_or_404(Customer, ip_address=ip_address)
    customer.subscription_status = False
    customer.save()
    return HttpResponse(status=200)

