from turtle import mode
from django.db import models
from django.forms import ImageField

# Create your models here.

class GalleryItem(models.Model):
    image = models.ImageField(upload_to="uploads/gallery_item")
    title = models.CharField(max_length=150)