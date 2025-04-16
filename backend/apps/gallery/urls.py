from django.urls import path
from . import views

urlpatterns = [
    path('gallery_details/<int:id>', views.gallery_details, name="gallery-details")
]
