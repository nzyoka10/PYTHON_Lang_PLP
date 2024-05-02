from django.db import models

# Create your models here.
# In Django, data is created in objects, called Models, and is actually tables in a database.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_data = models.DateField(null=True)  # Date without time