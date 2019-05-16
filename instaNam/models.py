from django.db import models

# Create your models here.

class Post(models.Model):
    contents = models.FileField(null=True)
    author = models.CharField(max_length=50, default = "")
    def __str__(self):  
       return str(self.contents)