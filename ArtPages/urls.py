from django.urls import path
from .views import IndexPageView, AboutPageView, OrderPageView, SchedulePageView, order_form

urlpatterns = [
    path("", IndexPageView, name="index"),
    path("about/", AboutPageView, name="About"),
    path("orders/", OrderPageView, name="Orders"),
    path("schedule/", SchedulePageView, name="Schedule"),
    path("<int:id>/", order_form, name="orderupdate"),
    path("prescriber/", orderPageView, name="prescriber"),
    path("orderform/", order_form, name="orderform"),
    path("orderlist/", order_list, name="orderlist"),
    path("delete/<int:id>/", views.order_delete, name="orderdelete")
]
