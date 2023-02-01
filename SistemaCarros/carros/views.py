import json
import os

from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView
from django.views.generic.list import ListView

from django.shortcuts import render, redirect

# Create your views here.
from Presupuestos.models import Presupuestos
from SistemaCarros import settings
from carros.forms import CarroForm
from carros.models import Carro
from django.core.files.storage import default_storage, FileSystemStorage

from invoices.models import Invoices


class IndexClassView(ListView):
    model=Carro
    template_name = 'carros/index.html'
    context_object_name='carros'
    queryset=Carro.objects.all()


def list_cars(request):

    if request.method == 'POST':
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Carro.objects.filter(fecha_registros__range=(fromdate, todate))
        return render(request,'carros/index.html',{'carros':searchresult})

    else:
        displaydata = Carro.objects.all()
    return render(request, 'carros/index.html', {'carros': displaydata})

def Imagedetail(request):
    car_id = request.POST.get('id')
    current_car = Carro.objects.get(id=car_id)
    return JsonResponse(json.dumps(list(json.loads(current_car.fotosCarro).keys())), safe=False)


class detail_carro(DetailView):
    template_name = 'carros/carros-detail.html'
    queryset=Carro.objects.all()
    context_object_name = 'carros'



class EditClassView(SuccessMessageMixin,UpdateView):
    model = Carro
    form_class=CarroForm
    template_name = 'carros/edit.html'
    success_url = reverse_lazy('carros:list_cars')
    success_message = "%(modelo)s this was updated successfully"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateView, self).get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if len(list(Presupuestos.objects.filter(carro_id=self.kwargs.get("pk"))))==0:
            context['invoices']=[]
            return context
        presupuestos_per_car = Presupuestos.objects.values_list('id').filter(carro_id=self.kwargs.get("pk"))
        car_range=[]
        for temp in presupuestos_per_car:
            car_range.append(temp[0])
        invoices_per_car=[]
        # for presupuesto in presupuestos_per_car:
        #     invoices_per_car.append(Invoices.objects.filter(estimate_id=presupuesto.id).first())
        context['invoices'] = Invoices.objects.filter(estimate_id__in=car_range)

        return context
#
class create_carros(SuccessMessageMixin,CreateView):
    model=Carro
    form_class=CarroForm
    template_name='carros/carros-form-add.html'
    success_url=reverse_lazy('carros:list_cars')
    success_message = "%(modelo)s this was created successfully"


#
def create_carros_picture(request):

        if request.FILES['files']:
            file = request.FILES['files']
            fs = FileSystemStorage()  # defaults to   MEDIA_ROOT
            new_name = "picture"
            new_name = fs.get_valid_name(new_name)+".jpg"
            filename = fs.save(new_name, file)
            return JsonResponse({filename:file.name},safe=False)
        else:
            form=CarroForm()
            return render(request, "carros/carros-form-add.html",{'form':form})


def create_carros_warranty(request):
    if request.FILES['files']:
        file = request.FILES['files']
        fs = FileSystemStorage()  # defaults to   MEDIA_ROOT
        ext = file.name.split('.')[-1]
        new_name = "warranty"
        new_name = fs.get_valid_name(new_name) + '.' + ext
        filename = fs.save(new_name, file)
        return JsonResponse({filename: file.name}, safe=False)
    else:
        form = CarroForm()
        return render(request, "carros/carros-form-add.html", {'form': form})


class delete_carro(DeleteView):
    model = Carro
    success_url=reverse_lazy('carros:list_cars') 

def detail_invoices(request, pk):
    invoice=Invoices.objects.get(pk=pk)
    presupuesto=Presupuestos.objects.get(pk=invoice.estimate_id)
    return render(request, "carros/invoice-detail.html",
                  {'presupuesto': presupuesto})



