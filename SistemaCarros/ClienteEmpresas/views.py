from django.shortcuts import render, redirect

# Create your views here.
from .forms import ClienteEmpresasForm


def create_ClienteEmpresas(request):
    form=ClienteEmpresasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clienteempresas:index')
    return render(request,'clienteempresas/clienteempresas-form.html',{'form':form})
