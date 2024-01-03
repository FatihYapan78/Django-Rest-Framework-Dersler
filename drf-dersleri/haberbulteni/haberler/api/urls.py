from django.urls import path,include
from haberler.api.views import *
urlpatterns = [
    path("gazeteciler/", GazeteciListCreateAPIView.as_view(), name="gazeteci-listesi"),
    path("haberler/", HaberListCreateAPIView.as_view(), name="haber-listesi"),
    path("haberler/<int:pk>", HaberDetailAPIView.as_view(), name="haber"),
]