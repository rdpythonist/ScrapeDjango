from django.urls import path
from .views import hello,APPDetailsAPI,AppDataViews

urlpatterns = [
    path("hello/",hello),
    path("appdetails/",APPDetailsAPI.as_view(),name='app_details'),
    path("applist/",AppDataViews.as_view(),name='applist')
]