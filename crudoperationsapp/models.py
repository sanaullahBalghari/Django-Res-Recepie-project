from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=60, default='')
    age = models.IntegerField()
    email = models.EmailField(default='')
    address = models.TextField(default='')

class product(models.Model):
    pass

class car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name