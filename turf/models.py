from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Turf(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    manager = models.OneToOneField(User, on_delete=models.CASCADE,related_name='manager')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='owner')
    price = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


