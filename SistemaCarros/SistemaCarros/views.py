from django.shortcuts import render, redirect
from Clientes.models import Clientes
from carros.models import Carro



def search(request):
    if request.method=="GET":
        searched=request.GET['searched']
        clientes=Clientes.objects.filter(nombre__icontains=searched)
        return render(request,'SistemaCarros/search.html',{'searched':searched,'clientes':clientes})
    else:
        return render(request,'SistemaCarros/search.html',{})




# def search(request):
#     if request.method=="GET":
#         searched=request.GET['searched']
#         clientes=Clientes.objects.filter(nombre__contains=searched)
#         return render(request,'SistemaCarros/search.html',{'searched':searched,'clientes':clientes})
#     else:
#         return render(request,'SistemaCarros/search.html',{})