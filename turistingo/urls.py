from django.urls import path
from turistingo import views

urlpatterns = [

    path('', views.turindex, name ='turindex'),


]