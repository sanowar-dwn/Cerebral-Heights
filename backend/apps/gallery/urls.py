from django.urls import path
from . import views

urlpatterns = [
    path('gallery_details/<int:id>', views.gallery_details, name="gallery-details"),
    path('', views.gallery_list, name="gallery_list"),
]
