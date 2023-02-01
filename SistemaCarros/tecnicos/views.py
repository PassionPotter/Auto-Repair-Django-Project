from django.contrib.messages.views import SuccessMessageMixin
from django.forms import formset_factory, modelform_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, FormView, DeleteView, DetailView

from Clientes.forms import ClientesForm
from Parte.forms import ParteForm
from tecnicos.forms import TecnicosForm
from tecnicos.models import Tecnicos



def tecnico_list(request):

    if request.method == 'POST':
        fromdate=request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Tecnicos.objects.filter(fecha_registro__range=(fromdate, todate))
        return render(request,'tecnicos/list.html',{'tecnicos':searchresult})

    else:
        disreplaydata = Tecnicos.objects.all()
    return render(request, 'tecnicos/list.html', {'tecnicos': disreplaydata})



class tecnicoIndex(ListView):
    model=Tecnicos
    template_name = 'tecnicos/list.html'
    context_object_name='tecnicos'
    queryset=Tecnicos.objects.all()

class addTecnico(SuccessMessageMixin,CreateView):
    model=Tecnicos
    form_class=TecnicosForm
    template_name='tecnicos/add.html'
    success_url=reverse_lazy('tecnicos:list_tecnicos')
    success_message = "%(nombreTecnico)s this is was created successfully"


class edit_inventory(UpdateView):
    model=Tecnicos
    form_class = TecnicosForm
    template_name='tecnicos/add.html'
    success_url=reverse_lazy('tecnicos:list_tecnicos')



class eliminar_tecnicos(DeleteView):
    model=Tecnicos
    success_url=reverse_lazy('tecnicos:list_tecnicos')
    context_object_name = 'tecnico'

class tecnicos_detail(DetailView):
    template_name = 'tecnicos/tecnicos-detail.html'
    queryset=Tecnicos.objects.all()
    context_object_name = 'tecnico'