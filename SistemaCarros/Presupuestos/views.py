import datetime

from django.forms import formset_factory, modelform_factory
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.template import loader

from django.contrib import messages
from Clientes.models import Clientes
from ManoObra.models import ManoObra
from Parte.models import Parte
from carros.models import Carro
from Pagos.models import Pagos
from invoices.models import Invoices
from tecnicos.models import Tecnicos
from .forms import PresupuestosClientesForm, PresupuestosVehiculosForm, PresupuestosParteForm, PresupuestosManoObraForm, \
    PresupuestosPagosForm, PresupuestosForm
 #Create your views here.
from .models import Presupuestos
from django.shortcuts import render, redirect
from django_xhtml2pdf.utils import generate_pdf
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.




def step1(request):
    presupuestosclientesform = PresupuestosClientesForm(request.POST)
    if request.method == 'POST':
        if presupuestosclientesform.is_valid():
            same_cliente = Clientes.objects.filter(correo=presupuestosclientesform.cleaned_data['correo'])
            if same_cliente:
                current_customer = same_cliente[0]
            else:
                isntance = presupuestosclientesform.save()
                current_customer = isntance

            presupuesto_instance=Presupuestos()
            presupuesto_instance.cliente_id=current_customer.id
            presupuesto_instance.save()
            request.session['presupuesto_id'] = presupuesto_instance.id
            request.session['client_id']=current_customer.id
            return redirect('Presupuestos:step2')

    return render(request,'Presupuestos/new-estimate-1-customer-details.html',{
        'presupuestosclientesform':presupuestosclientesform,

    })




def step2(request):
    presupuestosvehiculosform=PresupuestosVehiculosForm(request.POST or None)
    if request.method == 'POST':
        if presupuestosvehiculosform.is_valid():
            cd = presupuestosvehiculosform.cleaned_data
            same_car = Carro.objects.filter(placas=cd['placas'])
            if same_car:
                current_car = same_car[0]
            else:
                instance = presupuestosvehiculosform.save()
                current_car = instance

            request.session['car_id'] = current_car.id
            presupuesto_instance = Presupuestos.objects.get(pk=request.session['presupuesto_id'])
            presupuesto_instance.carro = current_car
            presupuesto_instance.save()
            return redirect('Presupuestos:step3')
    else:
        presupuestosvehiculosform=PresupuestosVehiculosForm(request.POST or None)

    return render(request,'Presupuestos/new-estimate-2-vehicle.html',{
        'presupuestosvehiculosform':presupuestosvehiculosform,

    })

def step3(request):
    extra_forms = 1
    ParteFormSet = formset_factory(PresupuestosParteForm, extra=extra_forms, max_num=20,can_delete=True)
    if request.method == 'POST':
        formset = ParteFormSet(request.POST, request.FILES, prefix='form')
        if formset.is_valid():
            for form in formset:
                if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate_id = Presupuestos.objects.get(pk=request.session['presupuesto_id'])
                    model_instance.save()
            presupuesto_instance = Presupuestos.objects.get(pk=request.session['presupuesto_id'])
            presupuesto_instance.resumen = request.POST['resumen']
            if (request.POST['descuento_parte'] == "Quantity"):
                presupuesto_instance.descuentoTotal_parte += float(request.POST['descuentoTotal_parte'])
            elif (request.POST['descuento_parte'] == "Percentage"):
                if not float(request.POST['descuentoTotal_parte']) == 0:
                    presupuesto_instance.descuentoTotal_parte += (100 - float(request.POST['descuentoTotal_parte'])) * float(
                        request.POST['total_parte']) / float(request.POST['descuentoTotal_parte'])
            presupuesto_instance.descuentoTotal_parte = round(presupuesto_instance.descuentoTotal_parte, 2)
            presupuesto_instance.total_parte += float(request.POST['total_parte'])
            presupuesto_instance.save()
            return redirect('Presupuestos:step4')
    else:
        formset = ParteFormSet()

    return render(request, 'Presupuestos/new-estimate-3-parts.html', {
        'formset': formset,
    })

def step4(request):
    extra_forms = 1
    ManoObraFormSet = formset_factory(PresupuestosManoObraForm, extra=extra_forms, max_num=20, can_delete=True)
    if request.method == 'POST':
        formset = ManoObraFormSet(request.POST, request.FILES, prefix='form')
        if formset.is_valid():
            for form in formset:
                if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate_ids = Presupuestos.objects.get(pk=request.session['presupuesto_id'])
                    model_instance.save()

            presupuesto_instance = Presupuestos.objects.get(pk=request.session['presupuesto_id'])
            if (request.POST['descuento_manaobra'] == "Quantity"):
                presupuesto_instance.descuentoTotal_manaobra += float(request.POST['descuentoTotal_manaobra'])
            elif(request.POST['descuento_manaobra'] == "Percentage"):
                if not float(request.POST['descuentoTotal_manaobra']) == 0:
                    presupuesto_instance.descuentoTotal_manaobra += (100 - float(request.POST['descuentoTotal_manaobra'])) * float(request.POST['total_manaobra'])/float(request.POST['descuentoTotal_manaobra'])
            presupuesto_instance.descuentoTotal_manaobra = round(presupuesto_instance.descuentoTotal_manaobra, 2)
            presupuesto_instance.total_manaobra += float(request.POST['total_manaobra'])
            presupuesto_instance.save()
            return redirect('Presupuestos:step5')
    else:
        formset = ManoObraFormSet()
    return render(request, 'Presupuestos/new-estimate-4-labor.html', {
        'formset': formset,

    })

def step5(request):
    Vehicle=Carro.objects.get(pk=request.session['car_id'])
    if request.method == 'POST':
        if request.POST['fotoscarro']:
            Vehicle.fotosCarro=request.POST['fotoscarro']
            Vehicle.save()
        return redirect('Presupuestos:step6')
    return render(request, 'Presupuestos/new-estimate-5-pictures.html')



def step6(request):
    extra_forms = 1
    ParteFormSet = formset_factory(PresupuestosPagosForm, extra=extra_forms, max_num=20, can_delete=True)
    if request.method == 'POST':
        formset = ParteFormSet(request.POST, request.FILES, prefix='form')
        if formset.is_valid():
            presupuesto_instance = Presupuestos.objects.get(pk=request.session['presupuesto_id'])
            for form in formset:
                if not form.cleaned_data["DELETE"]:
                    model_instance = form.save(commit=False)
                    model_instance.estimate = Presupuestos.objects.get(pk=request.session['presupuesto_id'])
                    presupuesto_instance.total_paid += round(float(model_instance.cantidad_pagada), 2)
                    presupuesto_instance.save()
                    model_instance.save()
            if presupuesto_instance.total_paid >= (presupuesto_instance.total_parte + presupuesto_instance.total_manaobra):
                presupuesto_instance.status = "PAID"
                presupuesto_instance.save()
            return redirect('Presupuestos:step7')
    else:
        formset = ParteFormSet(prefix='form')

    return render(request,'Presupuestos/new-estimate-6-payments.html',{
        'formset':formset
    })


#
def step7(request):
    step_estimate=Presupuestos.objects.get(pk=request.session['presupuesto_id'])
    technicans = Tecnicos.objects.all()
    step_client = Clientes.objects.get(pk=request.session['client_id'])
    step_vehicle = Carro.objects.get(pk=request.session['car_id'])
    step_parte=Parte.objects.filter(estimate_id=step_estimate.id)
    step_manoobra=ManoObra.objects.filter(estimate_ids=step_estimate.id)
    step_pago=Pagos.objects.filter(estimate_id=step_estimate.id)
    payment = 0
    for step in step_pago:
        payment += step.cantidad_pagada
    total = step_estimate.total_parte + step_estimate.total_manaobra
    balance = total - payment
    if request.method=='POST':
        if request.POST['technican_select']:
            step_estimate.tecnicos = Tecnicos.objects.get(pk=request.POST['technican_select'])
            step_estimate.save()
            return redirect('Presupuestos:step8')
    return render(request, 'Presupuestos/new-estimate-7-preview.html',
                  {'technicans': technicans, 'step_client': step_client, 'step_vehicle': step_vehicle,
                   'step_parte': step_parte, 'step_manoobra': step_manoobra, 'balance': balance, 'total': total,'step_estimate':step_estimate, 'payment':payment})


def step8(request):
    if request.method == 'POST':
        check_Invoice(request.session['presupuesto_id'])
        #request.session["messages"] = ["New Estimate is Added."]
        messages.success(request, "New Estimate is Added.")
        return redirect('Presupuestos:presupuestos')

    return render(request,'Presupuestos/new-estimate-8-confirm.html', )

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
                    presupuesto.total_paid += round(float(model_instance.cantidad_pagada),2)
                    model_instance.save()
            presupuesto.save()
            check_Invoice(pk)
            messages.success(request, "Payment is Added.")
            return redirect('Presupuestos:presupuestos')
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
                if not (float(request.POST['descuentoTotal_parte']) == 0):
                    presupuestos.descuentoTotal_parte += (100 - float(request.POST['descuentoTotal_parte'])) * float(request.POST['total_parte']) / float(request.POST['descuentoTotal_parte'])
            presupuestos.total_parte += float(request.POST['total_parte'])
            presupuestos.descuentoTotal_parte = round(presupuestos.descuentoTotal_parte, 2)
            presupuestos.save()
            messages.success(request, "Part is Added.")
        return redirect('Presupuestos:presupuestos')
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
            messages.success(request, "Labour is Added.")
        return redirect('Presupuestos:presupuestos')
    else:
        formset = ManoObraFormSet()
    return render(request, 'Presupuestos/estimate-add-labor.html', {
        'formset': formset,
    })


def presupuestosIndex(request):
    presupuestos_all = Presupuestos.objects.exclude(status='PAID')
    return render(request, "Presupuestos/presupuestos.html",
                  {'presupuestos': presupuestos_all})


def detail_presupuestos(request, pk):
    presupuesto = Presupuestos.objects.get(pk=pk)
    if request.method == 'POST':
        html_message = loader.render_to_string(
            'Presupuestos/estimate-pdf.html',
            {'presupuesto': presupuesto}
        )
        email_subject = 'Your Updated Estimate!'
        to_list = presupuesto.presupuesto.cliente.correo
        send_mail(email_subject, 'message', None, [to_list], fail_silently=False, html_message=html_message)
        messages.success(request, "Updated Estimate is sent by Email")
        return redirect('Presupuestos:presupuestos')
    else:
        return render(request, "Presupuestos/presupuestos-detail.html",
                  {'presupuesto': presupuesto})

def detail_in_pdf(request, pk):
    presupuesto = Presupuestos.objects.get(pk=pk)
    return render(request,"Presupuestos/estimate-pdf.html",{'presupuesto':presupuesto})

def cancel_presupuestos(request, pk):
    presupuesto = Presupuestos.objects.get(pk=pk)
    presupuesto.status = "CANCELED"
    presupuesto.save()
    messages.success(request, "Estimate is canceled")
    return redirect('Presupuestos:presupuestos')
def download_pdf(request,pk):
    # presupuesto = Presupuestos.objects.get(pk=pk)
    # return render(request, 'Presupuestos/estimate-pdf.html',{'presupuesto':presupuesto})
    presupuesto = Presupuestos.objects.get(pk=pk)
    context = {'presupuesto': presupuesto}
    result = generate_pdf('Presupuestos/estimate-pdf.html',context=context)

    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    filename = "Estimate_%s.pdf" % pk
    content = "attachment; filename=%s" % filename
    response['Content-Disposition'] = content
    return response

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

