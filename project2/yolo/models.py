from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    coordinates = models.JSONField(null=True, blank=True)
    labels = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
