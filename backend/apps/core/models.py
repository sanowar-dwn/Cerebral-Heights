from django.db import models
from django.forms import CharField


# Create your models here.
class Subject(models.Model):
    icon = models.ImageField(upload_to="uploads/subject_icon")
    title = models.CharField(max_length=50)


class SiteConfig(models.Model):
    logo = models.ImageField(upload_to="uploads/site_logo")
    phone_number = models.CharField(max_length=50)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    location = models.TextField()
    email_address = models.EmailField(max_length=254)
    site_title = models.CharField(max_length=50)
    fav_icon = models.ImageField(upload_to="uploads/fav_icon")
    header_text = models.CharField(max_length=50, blank=True, null=True)


class IndexBanner(models.Model):
    image = models.ImageField(upload_to="uploads/index_banner")
