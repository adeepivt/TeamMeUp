from django.db import models

# Create your models here.

class Turf(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField()
    manager = models.OneToOneField(User, on_delete=models.CASCADE)
    owner = models.ForeignKey()
    price = models.IntegerField()

    def __str__(self):
        return self.name


