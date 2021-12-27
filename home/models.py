from django.db import models

# Create your models here.
class Contact(models.Model):
    email= models.CharField(max_length=120,null=True)
    Name=models.CharField(max_length=120,null=True)
    LastName=models.CharField(max_length=120,null=True)
    city = models.CharField(max_length=120,null=True)
    date= models.DateField()

def __str__(self):
    return self.Name
