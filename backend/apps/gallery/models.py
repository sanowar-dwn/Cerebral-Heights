from django.db import models
from django.forms import ImageField



# Create your models here.

class GalleryItem(models.Model):
    image = models.ImageField(upload_to="uploads/gallery_item")
    title = models.CharField(max_length=150)


class GalleryItemImage(models.Model):
    gallery_item = models.ForeignKey("GalleryItem", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/gallery_item")