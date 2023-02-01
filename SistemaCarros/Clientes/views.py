from datetime import datetime

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect

#language


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from requests import request

from .forms import ClientesForm, DateRangeForm
from .models import Clientes
from django.contrib import messages



def list_clientes(request):

    from django.utils.translation import gettext as _
    # user_language='es'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY]=user_language
    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del request.session[translation.LANGUAGE_SESSION_KEY]
    # title=_('Homepage')
    if request.method == 'POST':
        fromdate=request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Clientes.objects.filter(fecha_registro__range=(fromdate, todate))
        return render(request,'Clientes/clientes-list.html',{'clientes':searchresult})

    else:
        displaydata = Clientes.objects.all()
    return render(request, 'Clientes/clientes-list.html', {'clientes': displaydata})


    # if request.method == 'POST':
    #     fromdate=request.POST.get('fromdate')
    #     todate = request.POST.get('todate')
    #     searchresult=Clientes.objects.raw('select nombre from Clientes where joindate between "'+fromdate+'" and "'+todate+'"')
    #     return render(request,'Clientes/clientes-list.html',{'clientes':searchresult})
    #
    # else:
    #     displaydata = Clientes.objects.all()
    # return render(request, 'Clientes/clientes-list.html', {'clientes': displaydata})



   #



#
# def list_clientes(request):
#
#     if request.method == 'POST':
#         form = DateRangeForm(request.POST)
#         # fromdate=request.POST.get('start_date')
#         # todate=request.POST.get('end_date')
#
#         if form.is_valid():
#             qs = Clientes.objects.filter(fecha_registro__range=(
#                 form.cleaned_data['start_date'],
#                 form.cleaned_data['end_date']
#             ))
#             return redirect('Clientes:clientes_list')
#     else:
#         clientes = Clientes.objects.all()
#         form=DateRangeForm()
#         return render(request,'Clientes/clientes-list.html',{'form':form, 'clientes':clientes})


#
# class list_clientes(ListView):
#     model=Clientes
#     template_name = 'Clientes/clientes-list.html'
#     context_object_name='clientes'
#     queryset=Clientes.objects.all()
#
#     #adicional
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context





class detail_clientes(DetailView):
    template_name = 'Clientes/clientes-detail.html'
    queryset=Clientes.objects.all()
    context_object_name = 'clientes'



class create_clientes(SuccessMessageMixin,CreateView):
    model=Clientes
    form_class = ClientesForm
    template_name='Clientes/clientes-add.html'
    success_url=reverse_lazy('Clientes:clientes_list')
    success_message = "New customer was created successfully"



class edit_clientes(UpdateView):
    model=Clientes
    form_class = ClientesForm
    template_name='Clientes/clientes-add.html'
    success_url=reverse_lazy('Clientes:clientes_list')

class eliminar_cliente(DeleteView):
    model=Clientes
    success_url=reverse_lazy('Clientes:clientes_list')
    context_object_name = 'clientes'
