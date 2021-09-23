from django.db import models

# Create your models here.
class Owner(models.Model):
    UserName=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    dp=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    photo=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    location=models.IntegerField()
    mobileno=models.TextField()
    email=models.EmailField( max_length=254)
    callAllowedTiming=models.CharField(max_length=50)
    desc=models.TextField()


class Tenant(models.Model):
    UserName=models.CharField(max_length=50)
    Id=models.CharField(max_length=50)
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    dp=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    photo=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    mobileno=models.TextField()
    email=models.EmailField(max_length=254)
    aadharNo=models.CharField(max_length=13)
    aadharPhoto=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    address=models.CharField(max_length=50)


class Room(models.Model):
    roomId=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    roomArea=models.CharField(max_length=50)
    rent=models.IntegerField()
    ownerid=models.IntegerField()
    photos=models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    maxAllowedPersonCount=models.IntegerField()
    roomstatus=models.BooleanField()
    gfbfAllowed=models.BooleanField()
    balkiniStatus=models.BooleanField()
    waterAvailability=models.BooleanField()
    OneBathroomSharedBy=models.IntegerField()
    OnWhichFloor=models.IntegerField()
    totalBathroom=models.IntegerField()
    totalBulbHolder=models.IntegerField()
    totalPlug=models.IntegerField()
    totalAlmirah=models.IntegerField()
    totalFans=models.IntegerField()
    totalwindows=models.IntegerField()
    totalChairs=models.IntegerField()
    totalTables=models.IntegerField()
    totalBed=models.IntegerField()
    pastReviews=models.TextField()




