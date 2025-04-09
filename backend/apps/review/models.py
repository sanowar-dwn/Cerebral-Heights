from turtle import mode
from django.db import models

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/review_images")
    text = models.TextField()