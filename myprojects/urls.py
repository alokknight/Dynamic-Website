from django.contrib import admin
from django.urls import path
from myprojects import views
#from app1 import views
urlpatterns = [
    path('',views.projects, name='projects'),
    # path('projects/',views.projects,name='projects'),
    # path('car_price_prediction/',views.myprojects, name='myprojects')
]