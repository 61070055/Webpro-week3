from django.contrib import admin
from django.urls import path

from check import views
urlpatterns = [
    path('check_stu/<int:stu_id>', views.check_stu),
    path('', views.index),
    path('qrcode/', views.qr)
]
