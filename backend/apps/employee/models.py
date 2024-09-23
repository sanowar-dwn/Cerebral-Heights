from django.db import models

# Create your models here.

class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="uploads/employee/profile_picture")
    designation = models.CharField(max_length=50)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    youtube = models.URLField(max_length=200, blank=True)
    banner = models.ImageField(upload_to="uploads/employee/banner")
    biography = models.TextField()
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.full_name