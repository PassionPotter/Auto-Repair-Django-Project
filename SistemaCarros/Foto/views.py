from django.shortcuts import render, redirect
from .forms import FotoForm

# Create your views here.

def create_Foto(request):
    form=FotoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('foto:index')
    return render(request,'Foto/foto-form.html',{'form':form})