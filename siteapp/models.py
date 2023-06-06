from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    coordinates = models.JSONField(null=True, blank=True)
    # Add any other fields you have in your Post model
    
    def __str__(self):
        return str(self.id)
