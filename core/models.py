from subprocess import REALTIME_PRIORITY_CLASS
from django import views
from django.db import models

class Realtor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Create your models here.
class Realestate(models.Model):
    title = models.CharField(max_length=120)
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories)
    publish_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title



