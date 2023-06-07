from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    Timestamp=models.DateTimeField(auto_now_add=True)
    Title=models.CharField(max_length=100,blank=False,null=True)
    Description=models.CharField(max_length=1000,blank=False,null=True)
    Status=models.CharField(max_length=10, choices=[('OPEN','OPEN'),('WORKING','WORKING'),('DONE','DONE'),('OVERDUE','OVERDUE')], default='OPEN', blank=False)
    Due_date=models.DateField(blank=True,null=True)
    Tags=models.CharField(max_length=1000,blank=True,null=True)
    def __str__(self):
        return self.Title


