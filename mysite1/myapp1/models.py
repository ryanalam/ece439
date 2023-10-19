from django.db import models
 
class Student(models.Model): # the name of class represent table name in database
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    profession = models.CharField(max_length = 255)
    telephone_number = models.IntegerField()
    email = models.EmailField()