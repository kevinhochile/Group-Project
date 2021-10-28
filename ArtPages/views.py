from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def IndexPageView(request):
    return HttpResponse('Welcome to Index')


def AboutPageView(request):
    return HttpResponse('About ME')


def OrderPageView(request):
    return HttpResponse('Order page')


def SchedulePageView(request):
    return HttpResponse('Schedule an app')
