from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    mob=models.BigIntegerField(blank=False,unique=True)
    email=models.EmailField(unique=True)
    usn=models.CharField(max_length=10,unique=True)
    college=models.CharField(max_length=100)
    degree=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    sem=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])