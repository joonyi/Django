from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'djangonautic/homepage.html')


def about(request):
    # return HttpResponse('about')
    return render(request, 'djangonautic/about.html')