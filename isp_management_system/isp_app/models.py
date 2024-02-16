from django.db import models

class ActiveCustomerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Customer(models.Model):
    ip_address = models.GenericIPAddressField(primary_key=True)
    bandwidth_allocation = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    subscription_status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = models.Manager()
    active_customers = ActiveCustomerManager()

    def __str__(self):
        return self.ip_address
