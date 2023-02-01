from django.shortcuts import render, redirect

# Create your views here.
from .forms import ManoObraForm


def create_ManoObra(request):
    form=ManoObraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('mano-obra:index')
    return render(request,'ManoObra/mano-obra-form.html',{'form':form}) 
