from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
# from .forms import ClientesForm
from .forms import InventoryForm
from .models import Inventory



def list_inventory(request):

    if request.method == 'POST':
        fromdate=request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Inventory.objects.filter(fecha_registro__range=(fromdate, todate))
        return render(request,'inventory/inventory-list.html',{'inventory':searchresult})

    else:
        displaydata = Inventory.objects.all()
    return render(request, 'inventory/inventory-list.html', {'inventory': displaydata})


#
# class list_inventory(ListView):
#     model=Inventory
#     template_name = 'inventory/inventory-list.html'
#     context_object_name='inventory'
#     queryset=Inventory.objects.all()



class create_inventory(SuccessMessageMixin,CreateView):
    model=Inventory
    form_class = InventoryForm
    template_name='inventory/inventory-add.html'
    success_url=reverse_lazy('inventory:list_inventory')
    success_message = "%(dealer)s this is was created successfully"


class edit_inventory(UpdateView):
    model=Inventory
    form_class = InventoryForm
    template_name='inventory/inventory-add.html'
    success_url=reverse_lazy('inventory:list_inventory')

class eliminar_inventory(DeleteView):
    model=Inventory
    success_url=reverse_lazy('inventory:list_inventory')
    context_object_name = 'inventory'


class detail_inventory(DetailView):
    template_name = 'inventory/inventory_detail.html'
    queryset=Inventory.objects.all()
    context_object_name = 'inventory'
