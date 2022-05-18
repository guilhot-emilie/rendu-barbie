from django.urls import path
from . import views

urlpatterns= [
    path('firstform/',views.firstform),
    path('traitement/',views.traitement),
    ]