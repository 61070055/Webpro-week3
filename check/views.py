from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def check_stu(request, stu_id):
    return HttpResponse('Student ID: %i' % stu_id)

def index(request):
    return HttpResponse("Welcome! This is Index Page.")

def qr(request):
    return HttpResponse("หน้าจอเช็คชื่อของแต่ละวิชาที่สามารถเช็คชื่อได้ด้วย QR code")
