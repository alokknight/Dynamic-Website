from django.urls import path
from calsum import views

urlpatterns = [

    path('', views.calculate, name ='calculate'),
    path('add/', views.add, name='add'),
    path('showcal/',views.showcal,name='showcal')

]