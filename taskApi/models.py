from django.db import models
from datetime import  datetime
from django.utils import timezone


# Create your models here.
class Tasks(models.Model):
    text = models.CharField(max_length=255)
    Day = models.DateField()
    time = models.TimeField()
    reminder = models.BooleanField(default=True)

    class Meta:
        verbose_name='Tasks'
        verbose_name_plural='Tasks'



    def __str__(self):
        return self.text