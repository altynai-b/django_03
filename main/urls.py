from django.urls import path
from .views import(
    home,
    index,
)

urlpatterns = [
    path('home/', home),
    path('index/', index),
]