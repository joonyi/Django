from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    note = models.TextField(blank=True)
    stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
