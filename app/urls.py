from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("shorten", views.UrlShortener.as_view(), name="shorten"),
    path("<str:short_url>" , views.UrlShortener.as_view(), name="redirect")
]