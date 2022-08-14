from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Gallery, Blog

def home(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')

def course(request, pk):
    c = Course.objects.get(id=pk)
    context = {
        'course': c,
    }
    return render(request, 'website/course.html', context)


def gallery(request):

    gallery_object = Gallery.objects.all()
    context = {
        'gallery_object': gallery_object,
    }

    return render(request, 'website/gallery.html', context)



def single_gallery(request, pk):
    c = Gallery.objects.get(id=pk)
    context = {
        'single_gallery': c,
    }
    return render(request, 'website/single-gallery.html', context)



def news(request):
    c = Blog.objects.all()
    context = {
        'news': c
    }
    return render(request, 'website/news.html', context)


def news_single(request, pk):
    c = Blog.objects.get(id=pk)
    b = Blog.objects.all()
    context = {
        'news_single': c,
        'news': b
    }
    return render(request, 'website/news-single.html', context)


def contact(request):
    return render(request, 'website/contact.html')