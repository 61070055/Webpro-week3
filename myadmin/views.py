from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def dashboard_stu(request):
    return HttpResponse('หน้าจอรายการนักเรียนทั้งหมด')

def add_stu(request):
    return HttpResponse('หน้าจอเพิ่มนักเรียน')

def edit_stu(request):
    return HttpResponse('หน้าจอแก้ไขข้อมูลนักเรียน')

def coruse(request):
    return HttpResponse('หน้าจอรายการวิชาเรียนทั้งหมด')

def add_coruse(request):
    return HttpResponse('หน้าจอเพิ่มวิชาเรียน')

def edit_coruse(request):
    return HttpResponse('หน้าจอแก้ไขข้อมูลวิชาเรียน')
