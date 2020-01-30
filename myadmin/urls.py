from django.contrib import admin
from django.urls import path
from myadmin import views
urlpatterns = [
    path('db_student/', views.dashboard_stu),
    path('add_student/', views.add_stu),
    path('edit_student/', views.edit_stu),
    path('coruse/', views.coruse),
    path('add_coruse', views.add_coruse),
    path('edit_coruse', views.edit_coruse)
]
