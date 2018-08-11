from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=3000)
    genre = models.CharField(max_length=100,blank=True,null=True)
    author = models.CharField(max_length=100, blank = True , null = True)
    age = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(4)
    ],blank=True, null=True)

    def __str__(self):
        return self.title
    
     

  



