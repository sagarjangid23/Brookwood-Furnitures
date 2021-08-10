from django.db import models

class Customer(models.Model):
    CustomerName = models.CharField(max_length=250, blank=True)
    CustomerEmailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    CustomerAddress = models.CharField(max_length=250, blank=True)
    CustomerColony = models.CharField(max_length=250, unique=True)
    CustomerCity = models.CharField(max_length=250, blank=True)
    CustomerPostcode = models.CharField(max_length=10, blank=True)
    CustomerCountry = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'Customer'
        ordering = ['-CustomerColony']

    def __str__(self):
        return str(self.CustomerName)

class Customer(models.Model):
    CustomerName = models.CharField(max_length=250, blank=True)
    CustomerEmailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    CustomerAddress = models.CharField(max_length=250, blank=True)
    CustomerColony = models.CharField(max_length=250, unique=True)
    CustomerCity = models.CharField(max_length=250, blank=True)
    CustomerPostcode = models.CharField(max_length=10, blank=True)
    CustomerCountry = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'Customer'
        ordering = ['-CustomerColony']

    def __str__(self):
        return str(self.CustomerName)