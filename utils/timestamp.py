from django.db import models

class TimeStampModel(models.Model): 
    created_at = models.DateTimeField(auto_now_add =True)
    modified_at = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True
        ordering = ['-modified_at','-created_at']

