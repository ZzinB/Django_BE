from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    coordinates = models.JSONField(null=True, blank=True)
    labels = models.ManyToManyField('Label', blank=True)
    
    def __str__(self):
        return str(self.id)
    
class Label(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
