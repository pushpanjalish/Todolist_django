from turtle import title
from django.db import models

# Create your models here.
class ToDo(models.Model):
    title=models.CharField(max_length=250)