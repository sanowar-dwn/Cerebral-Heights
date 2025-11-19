from ..employee.models import Employee
from ..gallery.models import GalleryItem
from ..review.models import Review
from .models import Subject, SiteConfig


def all_employees(request):
    return {"employee_all": Employee.objects.all()}


def all_gallery(request):
    return {"all_gallery": GalleryItem.objects.all()}


def all_review(request):
    return {"all_review": Review.objects.all()}


def all_subject(request):
    return {"all_subject": Subject.objects.all()}


def site_config(request):
    return {"site_config": SiteConfig.objects.all().first()}
