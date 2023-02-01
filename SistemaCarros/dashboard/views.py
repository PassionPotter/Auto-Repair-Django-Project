from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from InformacionTiendas.models import InformacionTiendas
from Clientes.models import Clientes
from Presupuestos.models import Presupuestos
from invoices.models import Invoices


def dashboard(request):

    month_name = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    workshop_count = InformacionTiendas.objects.count()
    customer_count = Clientes.objects.count()
    estimate_count = Presupuestos.objects.exclude(status="PAID").count()

    invoice_count = Invoices.objects.count()

    total_Revenu = 0
    graph_labels = []
    graph_data = []
    fromdate = datetime.now().date().strftime("%Y-%m-%d")
    todate = datetime.now().date().strftime("%Y-%m-%d")
    total_Invoice = 0
    if request.method == 'POST':
        if request.POST['fromdate']:
            fromdate = request.POST.get('fromdate')
        if request.POST['todate']:
            todate = request.POST.get('todate')
    if invoice_count:
        fromdate = Invoices.objects.order_by('-date_register')[0].date_register.date().strftime("%Y-%m-%d")
        todate = datetime.now().date().strftime("%Y-%m-%d 23:59:59")
        if request.method == 'POST':
            if request.POST['fromdate']:
                fromdate = request.POST.get('fromdate')
            if request.POST['todate']:
                todate= request.POST.get('todate') + " 23:59:59"
        invoices = Invoices.objects.filter(date_register__gte = fromdate, date_register__lte = todate)
        fromdate_year = int(fromdate[:4])
        fromdate_month = int(fromdate[5:7])
        fromdate_day = int(fromdate[8:10])

        todate_year = int(todate[:4])
        todate_month = int(todate[5:7])
        todate_day = int(todate[8:10])

        graph_labels = []
        graph_data = []
        if fromdate_year != todate_year:
            for x in range(fromdate_year, todate_year + 1):
                graph_labels.append(x)
                # data = Invoices.objects.filter(date_register__year=x).aggregate(Sum('amount'))['amount__sum']
                data = Invoices.objects.filter(date_register__year=x).count()
                if data == None:
                    data = 0
                total_Invoice += data
                graph_data.append(data)
        elif fromdate_month != todate_month:
            for x in range(fromdate_month, todate_month + 1):
                graph_labels.append(str(fromdate_year) + "/" + str(x))
                #data = Invoices.objects.filter(date_register__month=x).aggregate(Sum('amount'))['amount__sum']
                data = Invoices.objects.filter(date_register__month=x).count()
                if data == None:
                    data = 0
                total_Invoice += data
                graph_data.append(data)
        else:
            for x in range(fromdate_day, todate_day + 1):
                graph_labels.append(month_name[fromdate_month - 1] + " " + str(x))

                #data = Invoices.objects.filter(date_register__day=x).aggregate(Sum('amount'))['amount__sum']
                data = Invoices.objects.filter(date_register__day=x).count()
                if data == None:
                    data = 0
                total_Invoice += data
                graph_data.append(data)
        for invoice in invoices:
            total_Revenu+=invoice.amount
    return render(request, 'dashboard/dashboard.html', {'workshop_count':workshop_count,'customer_count':customer_count,'estimate_count':estimate_count,'total_Revenu':total_Revenu,
                                                        'graph_labels':graph_labels, 'graph_data':graph_data,
                                                        'from_date':fromdate,'to_date':todate, 'total_invoice':total_Invoice})