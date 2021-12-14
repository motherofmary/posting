from django.db import models
from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.title


    title=models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    date=models.DateField(default=datetime.date.today)
