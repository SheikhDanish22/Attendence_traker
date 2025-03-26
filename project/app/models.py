from django.db import models

# Create your models here.
class Admin(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    pass1=models.CharField(max_length=50)

class staff(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    gender=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    contact=models.IntegerField()
    branch=models.CharField(max_length=50)


class Attendence(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    gender=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    date=models.DateField()
    branch=models.CharField(max_length=50)
    
    
    

    