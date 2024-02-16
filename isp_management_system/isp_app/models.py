from django.db import models

class Customer(models.Model):
    ip_address = models.GenericIPAddressField(primary_key=True)
    name = models.CharField(max_length=100)
    subscription_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
