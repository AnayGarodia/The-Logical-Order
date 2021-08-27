from django.db import models

# Create your models here.


class Files(models.Model):
    image = models.FileField(upload_to='media')
    filename = models.CharField(max_length=255, default="devesh")
    date = models.CharField(max_length=255, default="devesh")
