from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User



class Task(models.Model):
    CHOICES_STATUS = {
        "cancel":"CANCELED",
        "proccessing": "PROCESS",
        "finish": "FINISH"
    }
    
    title = models.CharField(max_length=150)
    caption = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status =  models.CharField(max_length=100, choices=CHOICES_STATUS, default="proccessing")
    created_at = models.TimeField(default=datetime.now())
    
    def __str__(self):
        return self.title

