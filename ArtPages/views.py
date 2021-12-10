from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect, render, redirect
from django.http import HttpResponse
from ArtPages.forms import PrescriberForm
from ArtPages.models import Prescriber
from .forms import PrescriberForm
from .models import Prescriber
from .models import Drug
# from .models import Triple
from django.core.paginator import Paginator, EmptyPage


def IndexPageView(request):
    return render(request, 'ArtPages/index.html')


def AboutPageView(request):
    return render(request, 'ArtPages/about.html')


def OrderPageView(request):
    return render(request, 'ArtPages/order.html')


def SchedulePageView(request):
    return render(request, 'ArtPages/scheduling.html')


def prescriber_list(request):
    prescribers_lists = Prescriber.objects.all()
    p = Paginator(prescribers_lists, 60)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {'prescriber_list': page}
    return render(request, "opages/prescriber_list.html", context)


def prescriber_form(request, npi=0):

    if request.method == "GET":
        if npi == 0:
            form = PrescriberForm()
        else:
            prescriber = Prescriber.objects.get(pk=npi)
            form = PrescriberForm(instance=prescriber)
        return render(request, "opages/prescriber_form.html", {'form': form})
    else:
        if npi == 0:
            form = PrescriberForm(request.POST)
        else:
            prescriber = Prescriber.objects.get(pk=npi)
            form = PrescriberForm(request.POST, instance=prescriber)
        if form.is_valid():
            form.save()
        return redirect('/prescriberlist')


def prescriber_delete(request, npi):
    prescriber = Prescriber.objects.get(pk=npi)
    prescriber.delete()
    return redirect('/prescriberlist')
