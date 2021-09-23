from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=122,primary_key=True)
    phone=models.BigIntegerField()
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name



class Tutorial(models.Model):
    id=models.IntegerField(primary_key=True,default="")
    subject=models.CharField( default="xyz",max_length=100)
    img=models.ImageField( upload_to="pics",height_field=None, width_field=None, max_length=None)
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField()

    def __str__(self):
        return self.subject

