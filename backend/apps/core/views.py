import re
from django.shortcuts import render
from .models import IndexBanner


# Create your views here.
def index(request):
    index_banners = IndexBanner.objects.all()
    context = {"index_banners": index_banners}
    return render(request, "index.html", context)


def contact_us(request):
    return render(request, "contact-us.html")
