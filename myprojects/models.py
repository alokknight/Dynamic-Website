from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Project(models.Model):
    title=models.CharField( max_length=150)
    img=models.ImageField(upload_to="pics", height_field=None, width_field=None, max_length=None)
    startingdate=models.DateField()
    endingdate=models.DateField()
    techused=models.CharField( max_length=50)
    desc=models.TextField()

    def __str__(self):
        return self.title