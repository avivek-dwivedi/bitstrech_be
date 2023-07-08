from django.contrib import admin
from django.urls import path,re_path,include
from data_loader import views

urlpatterns = [
  
    re_path('uplo/',views.upload_view)
]
