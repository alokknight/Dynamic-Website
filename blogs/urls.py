from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.blog,name='blog'),
    path('blog1/',views.blog1,name='blog1')
    
]
