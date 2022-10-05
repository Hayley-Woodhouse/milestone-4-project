from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=260)
    friendly_name = models.CharField(max_length=260, null=True, blank=True)

    def __self__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=260, null=True, blank=True)
    name = models.CharField(max_length=260)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __self__(self):
        return self.name
