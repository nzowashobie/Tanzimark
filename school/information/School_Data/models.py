from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
        #user = models.ForeignKey(User, on_delete = models.CASCADE)
        password = models.CharField(max_length=200)
        name = models.CharField(max_length=200)
        Subject = models.CharField(max_length=200)
        Grade = models.CharField(max_length=200)
        IMAGES = models.FileField(upload_to='photo/')
        def __str__(self):
            return self.name
       # class Meta:
           # db_table = "SLIPS"

class Users(models.Model):
        username = models.CharField(max_length=200)
        Phone_no = models.CharField(max_length=200)
        password1 = models.CharField(max_length=200)
        password2 = models.CharField(max_length=200)
       
        def __str__(self):
            return self.username
        class Meta:
            db_table = "Register"


class Infor_school(models.Model):
        name = models.CharField(max_length=200)
        bio = models.CharField(max_length=200)
        picz = models.FileField(upload_to='bio_image/')
       
        def __str__(self):
            return self.name
      
      

