from django.contrib import admin
from .models import GalleryItem, GalleryItemImage

class GalleryItemImageInline(admin.TabularInline):
    model = GalleryItemImage
    extra = 1  # number of empty forms to display

class GalleryItemAdmin(admin.ModelAdmin):
    inlines = [GalleryItemImageInline]

admin.site.register(GalleryItem, GalleryItemAdmin)
