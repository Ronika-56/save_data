from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=50, unique=True)
    dob = models.DateField()
    weight = models.IntegerField(default=50)
    height = models.FloatField(default=1.6)
    gender = models.CharField(max_length=50, default='male')
    class Meta:
        db_table = 'person'

#python manage.py makemigrations
#python manage.py migrate