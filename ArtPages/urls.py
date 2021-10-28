from django.urls import path
from .views import IndexPageView, AboutPageView, OrderPageView, SchedulePageView

urlpatterns = [
    path("", IndexPageView, name="index"),
    path("about/", AboutPageView, name="About"),
    path("orders/", OrderPageView, name="Orders"),
    path("schedule/", SchedulePageView, name="Schedule")
]
