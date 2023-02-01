from django.core.mail import send_mail
from django.forms import formset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import TemplateView, ListView
import json
# from inventory.models import Inventory
from ManoObra.models import ManoObra
from Presupuestos.forms import PresupuestosPagosForm, PresupuestosParteForm, PresupuestosForm, PresupuestosManoObraForm
from Presupuestos.models import Presupuestos
from carros.models import Carro
from invoices.models import Invoices
from tecnicos.models import Tecnicos
from .forms import ReporteTechnicianForm
from django.db.models import Count, Sum
from django.contrib import  messages
# Create your views here.
from .models import ReporteGanancias, ReporteTechnician
from .models import Parte
from datetime import datetime

class IndexReporteGanancias(TemplateView):
    template_name='ReporteGanancias/list.html'



def reportsDebtors(request):
    if request.method =='POST':
        fromdate=request.POST['fromdate'] + " 00:00:00"
        todate=request.POST['todate'] + " 23:59:59"
        presupuestos_all=Presupuestos.objects.filter(register_time__range=(fromdate,todate), status="PENDING")
    else:
        presupuestos_all = Presupuestos.objects.filter(status="PENDING")
        fromdate = datetime.now().date().strftime("%Y-%m-%d")
        todate = datetime.now().date().strftime("%Y-%m-%d")
    return render(request, "ReporteGanancias/reports-debtors.html",
                  {'presupuestos': presupuestos_all, 'fromdate':fromdate, 'todate':todate})

def send_email(request,pk):
    presupuesto = Presupuestos.objects.get(pk=pk)
    html_message = loader.render_to_string(
        'Presupuestos/estimate-pdf.html',
        {'presupuesto': presupuesto}
    )
    email_subject = 'Your Estimate!'
    to_list = presupuesto.presupuesto.cliente.correo
    send_mail(email_subject, 'message', None, [to_list], fail_silently=False, html_message=html_message)
    messages.success(request, "Updated Estimate is sent by Email")
    return redirect('ReporteGanancias:debtors')
def addPay(request, pk):
    extra_forms = 1
    ParteFormSet = formset_factory(PresupuestosPagosForm, extra=extra_forms, max_num=20, can_delete=True)
    if request.method == 'POST':
        formset = ParteFormSet(request.POST, request.FILES, prefix='form')
        presupuesto = Presupuestos.objects.get(pk=pk)
        if formset.is_valid():
            for form in formset:
                if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate = Presupuestos.objects.get(pk=pk)
                    presupuesto.total_paid += round(model_instance.cantidad_pagada,2 )
                    model_instance.save()
            presupuesto.save()
        check_Invoice(pk)
        messages.success(request, "Payment is Added")
        return redirect('ReporteGanancias:debtors')
    else:
        formset = ParteFormSet()
    return render(request, 'Presupuestos/estimate-add-payment.html', {
        'formset': formset,
    })



def addPart(request, pk):
    extra_forms = 1
    ParteFormSet = formset_factory(PresupuestosParteForm, extra=extra_forms, max_num=20, can_delete=True)
    presupuestos = Presupuestos.objects.filter(id=pk).values()[0]
    presupuestosForm = PresupuestosForm(initial=presupuestos)
    if request.method == 'POST':
        formset = ParteFormSet(request.POST, request.FILES, prefix='form')
        if formset.is_valid():
            for form in formset:
                if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate_id = Presupuestos.objects.get(pk=pk)
                    model_instance.save()

            presupuestos = Presupuestos.objects.get(pk=pk)

            if (request.POST['descuento_parte'] == "Quantity"):
                presupuestos.descuentoTotal_parte += float(request.POST['descuentoTotal_parte'])
            elif(request.POST['descuento_parte'] == "Percentage"):
                if not float(request.POST['descuentoTotal_parte']) == 0:
                    presupuestos.descuentoTotal_parte += (100 - float(request.POST['descuentoTotal_parte'])) * float(request.POST['total_parte']) / float(request.POST['descuentoTotal_parte'])
            print(float(request.POST['total_parte']))
            presupuestos.total_parte += float(request.POST['total_parte'])
            presupuestos.descuentoTotal_parte = round(presupuestos.descuentoTotal_parte, 2)

            presupuestos.save()
            messages.success(request, "part is Added")
        return redirect('ReporteGanancias:debtors')
    else:
        formset = ParteFormSet()

    return render(request, 'Presupuestos/estimate-add-parts.html', {
        'presupuestosForm': presupuestosForm,
        'formset': formset,
    })



def addLabor(request, pk):
    extra_forms = 1
    ManoObraFormSet = formset_factory(PresupuestosManoObraForm, extra=extra_forms, max_num=20, can_delete=True)
    if request.method == 'POST':
        formset = ManoObraFormSet(request.POST, request.FILES, prefix='form')

        if formset.is_valid():
            for form in formset:
                if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate_ids = Presupuestos.objects.get(pk=pk)
                    model_instance.save()
            presupuestos = Presupuestos.objects.get(pk=pk)

            if (request.POST['descuento_manaobra'] == "Quantity"):
                presupuestos.descuentoTotal_manaobra += float(request.POST['descuentoTotal_manaobra'])
            elif(request.POST['descuento_manaobra'] == "Percentage"):
                if not float(request.POST['descuentoTotal_manaobra']) == 0:
                    presupuestos.descuentoTotal_manaobra += (100 - float(request.POST['descuentoTotal_manaobra'])) * float(request.POST['total_manaobra'])/float(request.POST['descuentoTotal_manaobra'])
            presupuestos.total_manaobra += float(request.POST['total_manaobra'])
            presupuestos.descuentoTotal_manaobra = round(presupuestos.descuentoTotal_manaobra, 2)
            presupuestos.save()
            messages.success(request, "Labour is Added")
        return redirect('ReporteGanancias:debtors')
    else:
        formset = ManoObraFormSet()
    return render(request, 'Presupuestos/estimate-add-labor.html', {
        'formset': formset,
    })


def pendingStock(request):

    if request.method == 'POST':
        fromdate=request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Parte.objects.filter(fecha_registro__range=(fromdate, todate))
        queryset = Parte.objects.filter(quantity__lt=10)
        return render(request,'ReporteGanancias/reports-pending-stock.html',{'parte':searchresult,'queryset':queryset})

    else:
        displaydata = Parte.objects.all()
    return render(request, 'ReporteGanancias/reports-pending-stock.html', {'parte': displaydata,'queryset':queryset})


class pendingStock(ListView):
    model=Parte
    template_name = 'ReporteGanancias/reports-pending-stock.html'
    context_object_name='parte'
    queryset = Parte.objects.filter(quantity__lt=10)


class Records(TemplateView):

    template_name = 'ReporteGanancias/reports-records.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invoices = []
        carros_list = Invoices.objects.values('estimate__carro__id').distinct()
        for carros in carros_list:
            for invoice in Invoices.objects.filter(estimate__carro__id = carros['estimate__carro__id']):
                invoices.append(invoice)
        context['invoices'] = invoices
        return context
def ViewInvoice(request,pk):
    invoice=Invoices.objects.get(pk=pk)
    presupuesto =  Presupuestos.objects.get(pk=invoice.estimate_id)
    return render(request,'ReporteGanancias/reports-invoice-detail.html',{'invoice':invoice,'presupuesto':presupuesto})
def Technicians(request):

    if request.method=="POST":
        fromdate = request.POST['fromdate'] + " 00:00:00"
        todate = request.POST['todate'] + " 23:59:59"
        estimates = Presupuestos.objects.filter(register_time__range=(fromdate, todate))
    else:
        estimates = Presupuestos.objects.all()
        fromdate = datetime.now().date().strftime("%Y-%m-%d") + " 00:00:00"
        todate = datetime.now().date().strftime("%Y-%m-%d") + " 00:00:00"
    tech_estimates = []
    count = 0
    for estimate in estimates:
        technicians_ids = []
        technicians = []
        for labour in estimate.manoobra_set.values():
            id = ManoObra.objects.get(pk=labour['id']).tecnico.id
            if not id in technicians_ids:
                technicians_ids.append(id)
        for tech_id in technicians_ids:
            technicians_mano = []
            sum = 0
            for labour in estimate.manoobra_set.filter(tecnico__id=tech_id).values():
                technicians_mano.append(ManoObra.objects.get(pk=labour['id']))
                sum += labour["tarifa_total"]
            technicians.append({'labour':technicians_mano, 'sum':sum, 'count':count})

        tech_estimates.append({
            "presupuesto": estimate,
            "labours": technicians,
            'labour_count':count,
        })
        count += len(technicians)

    return render(request, "ReporteGanancias/reports-technicians.html", {"estimates":tech_estimates, "fromdate":fromdate, "todate":todate})
    # queryset=Presupuestos.objects.all()


def Workshops(request):
    template_name = 'ReporteGanancias/reports-workshops.html'

    if request.method =='POST':
        fromdate=request.POST['fromdate'] + " 00:00:00"
        todate=request.POST['todate'] + " 23:59:59"
        carros = Presupuestos.objects.filter(register_time__range=(fromdate, todate)).values_list('carro_id').annotate(
            truck_count=Count('carro_id')).order_by('-truck_count')[:10]
        manoobras = ManoObra.objects.filter(estimate_ids__register_time__range=(fromdate, todate)).values_list('codigo').annotate(truck_count1=Count('id')).order_by('-truck_count1')[
                    :10]
        partes = Parte.objects.filter(estimate_id__register_time__range=(fromdate, todate)).values_list('codigo').annotate(truck_count1=Count('id')).order_by('-truck_count1')[:10]
    else:
        carros = Presupuestos.objects.values_list('carro_id').annotate(truck_count=Count('carro_id')).order_by('-truck_count')[:10]
        manoobras = ManoObra.objects.values_list('codigo').annotate(truck_count1=Count('id')).order_by('-truck_count1')[:10]
        partes = Parte.objects.values_list('codigo').annotate(truck_count1=Count('id')).order_by('-truck_count1')[:10]
        fromdate = datetime.now().date().strftime("%Y-%m-%d") + " 00:00:00"
        todate = datetime.now().date().strftime("%Y-%m-%d") + " 00:00:00"
    cars=[]
    for carro in carros:
        if carro[0]==None:
            break
        cars.append(Carro.objects.get(pk=carro[0]))

    labors=[]
    for manoobra in manoobras:
        labors.append(ManoObra.objects.filter(codigo=manoobra[0])[0])
    parts=[]
    for part in partes:
        parts.append(Parte.objects.filter(codigo=part[0])[0])
    return render(request, "ReporteGanancias/reports-workshops.html", { 'cars':cars, 'labors':labors, 'parts':parts, 'fromdate':fromdate, 'todate':todate})

def techniciansAddPayment(request, estimate, technico):
    technicianForm = ReporteTechnicianForm(request.POST)
    if request.method=="POST":
        if technicianForm.is_valid():
            cd = technicianForm.cleaned_data
            technician_instance = ReporteTechnician()
            technician_instance.estimate = Presupuestos.objects.get(pk=estimate)
            technician_instance.technician = Tecnicos.objects.get(pk=technico)
            technician_instance.content = cd["content"]
            technician_instance.quantity = round(cd["quantity"],2)
            technician_instance.save()
            return redirect('ReporteGanancias:technicians')
    return render(request, 'ReporteGanancias/reports-technicians-add-payment.html', {'technicianForm':technicianForm})

def techniciansViewPayment(request, estimate, technico, percent, total):
    estimate_instance = Presupuestos.objects.get(pk=estimate)
    technician = Tecnicos.objects.get(pk=technico)
    reports_payment = ReporteTechnician.objects.filter(estimate__id=estimate, technician__id=technico)

    labours = []
    for labour in estimate_instance.manoobra_set.filter(tecnico__id=technico).values():
        labours.append(ManoObra.objects.get(pk=labour['id']))
    sum = 0
    for payment in reports_payment:
        sum += payment.quantity
    return render(request, "ReporteGanancias/reports-technicians-view-payment.html", {
        "estimate":estimate_instance,
        "technician":technician, "paymentlist":reports_payment, "labours":labours, "percent":percent, "total":total, "sum":sum
    })


def check_Invoice(id):
    presupuestos = Presupuestos.objects.get(pk=id)
    if presupuestos.total_paid >= (presupuestos.total_parte + presupuestos.total_manaobra):
        presupuestos.status = "PAID"
        invoice_instance = Invoices()
        invoice_instance.estimate = presupuestos
        invoice_instance.amount = presupuestos.total_paid
        invoice_instance.status = "PAID"
        invoice_instance.save()
    presupuestos.save()

def DeletePayment(request, id):
    print(id)
    ReporteTechnician.objects.get(pk=id).delete()
    messages.success(request, "Payment is Deleted successfully.")
    return redirect("ReporteGanancias:technicians")
 
