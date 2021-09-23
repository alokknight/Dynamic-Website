from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=122,primary_key=True,default="xyz")
    firstname=models.CharField(max_length=122,default="xyz")
    lastname=models.CharField(max_length=122,default="xyz")
    email=models.EmailField(max_length=122,default="xyz@gmail.com")
    password=models.CharField(max_length=20)
    phone=models.BigIntegerField(default="000")
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.username