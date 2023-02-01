from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
# from .forms import ClientesForm
from Parte.forms import ParteForm
from Parte.models import Parte


def list_parte(request):

    if request.method == 'POST':
        fromdate=request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Parte.objects.filter(fecha_registro__range=(fromdate, todate))
        return render(request,'Parte/part-list.html',{'parte':searchresult})

    else:
        displaydata = Parte.objects.all()
    return render(request, 'Parte/part-list.html', {'parte': displaydata})


#
# class list_inventory(ListView):
#     model=Inventory
#     template_name = 'inventory/part-list.html'
#     context_object_name='inventory'
#     queryset=Inventory.objects.all()



class create_parte(SuccessMessageMixin,CreateView):
    model=Parte
    form_class = ParteForm
    #context_object_name = 'partes'
    template_name='Parte/part-add.html'
    success_url=reverse_lazy('parte:list_parte')
    success_message = "%(dealer)s this is was created successfully"


class edit_parte(UpdateView):
    model=Parte
    form_class = ParteForm
    template_name='Parte/part-add.html'
    success_url=reverse_lazy('parte:list_parte')

class eliminar_parte(DeleteView):
    model=Parte
    success_url=reverse_lazy('parte:list_parte')
    context_object_name = 'part'


class detail_parte(DetailView):
    template_name = 'Parte/part-detail.html'
    queryset=Parte.objects.all()
    context_object_name = 'part'



