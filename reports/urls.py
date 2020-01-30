from django.contrib import admin
from django.urls import path
from reports import views
urlpatterns = [
    path('', views.dashboard),
    path('find', views.find)
]
