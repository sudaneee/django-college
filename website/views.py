from django.shortcuts import render
from .models import Carousel

# Create your views here.

def home(request):

    general_info = Carousel.objects.all()
    context = {
        'general_info': general_info,
    }

    return render(request, 'website/index.html', context)