from django.urls import path,include
from haberler.api.views import *
urlpatterns = [
    path("haberler/", HaberListCreateAPIView.as_view(), name="haber-listesi"),
    path("haberler/<int:id>", HaberDetailAPIView.as_view(), name="haber"),
]