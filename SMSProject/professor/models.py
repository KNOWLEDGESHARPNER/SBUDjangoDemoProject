from django.db import models

# Create your models here.
class Professor(models.Model):
    name=models.CharField(max_length=100)
    mob=models.BigIntegerField(blank=False,unique=True)
    email=models.EmailField(unique=True)
    department=models.CharField(max_length=100,unique=True)
    college=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    experiance=models.IntegerField()

    def __str__(self):
        return self.name