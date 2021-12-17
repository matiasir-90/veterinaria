from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    #return HttpResponse('vista inicio')
    return  render (request,'veterinaria1/inicio.html') 
def animal(request):
    #return HttpResponse('vista animal')
    return  render (request,'veterinaria1/animal.html') 
def doctor(request):
    #return HttpResponse('vista doctor')
    return  render (request,'veterinaria1/doctor.html') 
def cliente(request):
    #return HttpResponse('vista cliente')
    return  render (request,'veterinaria1/cliente.html') 