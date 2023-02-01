from django.shortcuts import render, redirect

# Create your views here.
from .forms import PagosForm


def create_Pagos(request):
    form=PagosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('parte:index')
    return render(request,'Pagos/pagos-form.html',{'form':form}) 

