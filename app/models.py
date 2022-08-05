from tkinter import CASCADE
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse


class guide(models.Model):    
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
class page(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    guidename=models.CharField(max_length=255,null=True,blank=True)
class section(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    guidename=models.CharField(max_length=255, null=True,blank=True)
    pagename=models.CharField(max_length=255,null=True, blank=True )


