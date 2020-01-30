from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def dashboard(request):
    return HttpResponse('This is Dashboard')

def find(request):
    return HttpResponse('หน้าจอค้นหา และ export ข้อมูลการเข้าห้องเรียน ทั้งในเทอมปัจจุบัน และ ย้อนหลัง')

