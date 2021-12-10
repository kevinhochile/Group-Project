from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect, render, redirect
from django.http import HttpResponse
from ArtPages.forms import OrderForm
from ArtPages.models import Order
from .forms import OrderForm
from .models import Order

from django.core.paginator import Paginator, EmptyPage


def IndexPageView(request):
    return render(request, 'ArtPages/index.html')


def AboutPageView(request):
    return render(request, 'ArtPages/about.html')


def OrderPageView(request):
    return render(request, 'ArtPages/order.html')


def SchedulePageView(request):
    return render(request, 'ArtPages/scheduling.html')


def order_list(request):
    prescribers_lists = Order.objects.all()
    p = Paginator(order_lists, 60)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {'order_list': page}
    return render(request, "ArtPages/order_list.html", context)


def order_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = OrderForm()
        else:
            prescriber = Order.objects.get(pk=id)
            form = OrderForm(instance=prescriber)
        return render(request, "ArtPages/order_form.html", {'form': form})
    else:
        if id == 0:
            form = OrderForm(request.POST)
        else:
            prescriber = Order.objects.get(pk=id)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('/orderlist')


def order_delete(request, id):
    order = Order.objects.get(pk=id)
    order.delete()
    return redirect('/orderlist')
