from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
from .forms import DetalleForm


def create_Detalle(request):
    form=DetalleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('detalle:index')
    return render(request,'Detalle/detalle-form.html',{'form':form})

