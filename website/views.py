from django.http import HttpResponse
from django.shortcuts import render

from .models import Hello, Performance, Writing

# Create your views here.
# def home(request):
#     return render(request, '')

def home(request):
    return render(request, 'website/home.html')

def hello(request):
    hello_data = Hello.objects.all()[0]
    context = {'data': hello_data, 'page': 'hello'}
    return render(request, 'website/hello.html', context)

def performance(request):
    performance_data = Performance.objects.all()[0]
    links = performance_data.links.all()
    context = {'data': performance_data, 'links': links, 'page': 'performance'}
    return render(request, 'website/performance.html', context)

def writing(request):
    writing_data = Writing.objects.all()[0]
    links = writing_data.links.all()
    context = {'data': writing_data, 'links': links, 'page': 'writing'}
    return render(request, 'website/writing.html', context)
