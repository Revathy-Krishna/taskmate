from django.db import models


# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=45)
    done = models.BooleanField(default=False)