from django.shortcuts import render
from .models import GalleryItem, GalleryItemImage
# Create your views here.

def gallery_details(request, id):
    gallery_item = GalleryItem.objects.get(id=id)
    gallery_item_images = GalleryItemImage.objects.filter(gallery_item=gallery_item)
    context = {
        'gallery_item':gallery_item,
        'gallery_item_images':gallery_item_images,
    }
    return render(request, 'gallery-details.html', context)