from django.shortcuts import render
from .models import Review


# Create your views here.
def review_list(request):
    review_all = Review.objects.all()
    context = {
        "review_all": review_all,
    }
    return render(request, "review-list.html", context)
