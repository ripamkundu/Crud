from django.db import models

# Create your models here.
class user_insert(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
 
    class Meta:
        db_table="User_insert"