from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    # path('projects/',views.projects,name='projects'),
    path('blogs/',views.blogs,name='blogs'),
    path('tutorial/', views.tutindex, name ='tutindex')


]
