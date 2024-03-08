from django.db import models

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    birth_day=models.DateField(blank=True,null=True)
    email = models.EmailField(max_length=100)
    password= models.CharField(max_length=100)

    def __str__(self):
        return self.email

