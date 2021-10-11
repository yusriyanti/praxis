from django.db import models

# Create your models here.
class Makanan(models.Model):
    name=models.CharField(default='',max_length=20)