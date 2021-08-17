from django.db import models

# Create your models here.


class Files(models.Model):
    image = models.FileField(upload_to='media')
    name = models.CharField(max_length=255, default="devesh")
    gender = models.CharField(max_length=10, default="male")
    age = models.IntegerField(default=20)
    filename = models.CharField(max_length=255, default="devesh")
    user = models.CharField(max_length=255, default="devesh")
    date = models.CharField(max_length=255, default="devesh")
