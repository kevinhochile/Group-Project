from django.urls import path
from .views import IndexPageView, AboutPageView, OrderPageView, SchedulePageView

urlpatterns = [
    path("", IndexPageView, name="index"),
    path("about/", AboutPageView, name="About"),
    path("orders/", OrderPageView, name="Orders"),
    path("schedule/", SchedulePageView, name="Schedule")
]

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("prescriber/", prescriberPageView, name="prescriber"),
    path("<int:npi>/", prescriber_form, name="prescriberupdate"),
    path("prescriberform/", prescriber_form, name="prescriberform"),
    path("prescriberlist/", prescriber_list, name="prescriberlist"),
    path("delete/<int:npi>/", views.prescriber_delete, name="prescriberdelete"),
    path("prescribersearch/", PrescriberSearchPageView, name="prescribersearch"),
    path("searchpres/", searchPageView, name="searchpres"),
    path("drugsearch/", drugPageView, name="drugsearch"),
    path("searchdrug/", searchDrugPageView, name="searchdrug"),
    path("prediction/", predictionPageView, name="prediction"),
    path("recommender/", recommenderPageView, name="recommender")
]
