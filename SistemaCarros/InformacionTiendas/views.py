from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, DeleteView, DetailView

from .forms import InformacionTiendasForm
from .models import InformacionTiendas



class IndexClassView(ListView):
    model=InformacionTiendas
    template_name = 'InformacionTiendas/index.html'
    context_object_name='tiendas'
    queryset=InformacionTiendas.objects.all()



class EditClassView(UpdateView):
    model =InformacionTiendas
    template_name= 'InformacionTiendas/informacion-tiendas-agregar.html'
    form_class=InformacionTiendasForm
    success_url = reverse_lazy('InformacionTiendas:list_tiendas')



class InformacionTiendasAdd(SuccessMessageMixin,CreateView):
    model=InformacionTiendas
    form_class=InformacionTiendasForm
    template_name='InformacionTiendas/informacion-tiendas-agregar.html'
    success_url=reverse_lazy('InformacionTiendas:list_tiendas')
    success_message = "%(nombre_taller)s this is was created successfully"
    #context_object_name = 'tiendas'




class eliminar_tiendas(DeleteView):
    model=InformacionTiendas
    success_url=reverse_lazy('InformacionTiendas:list_tiendas')
    context_object_name = 'tiendas'

class tiendas_detail(DetailView):
    template_name = 'InformacionTiendas/informacion-tiendas-detail.html'
    queryset=InformacionTiendas.objects.all()
    context_object_name = 'tiendas'





