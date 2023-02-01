from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView
from django_xhtml2pdf.utils import generate_pdf
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView
from Presupuestos.models import Presupuestos
from invoices.models import Invoices
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from tecnicos.models import Tecnicos


class list_invoices(ListView):
    model=Invoices
    template_name = 'invoices/list.html'
    context_object_name='invoices'
    queryset=Invoices.objects.all()

def detail_invoices(request, pk):
    invoice = Invoices.objects.get(pk=pk)
    presupuesto=Presupuestos.objects.get(pk=invoice.estimate_id)
    if request.method == 'POST':
        html_message = loader.render_to_string(
            'invoices/invoice-pdf.html',
            {'presupuesto': presupuesto}
        )
        email_subject = 'Your Updated Invoice!'
        to_list = presupuesto.cliente.correo
        send_mail(email_subject, 'message', None, [to_list], fail_silently=False, html_message=html_message)

        messages.success(request,"Updated Invoice is sent by Email" )
        return redirect('invoices:list')
    else:
        return render(request, "invoices/invoice-detail.html",
                  {'presupuesto': presupuesto})
def download_pdf(request,pk):
    invoice=Invoices.objects.get(pk=pk)
    presupuesto = Presupuestos.objects.get(pk=invoice.estimate_id)
    context = {'presupuesto': presupuesto}
    result = generate_pdf('Presupuestos/estimate-pdf.html',context=context)

    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    filename = "Invoice_%s.pdf" % pk
    content = "attachment; filename=%s" % filename
    response['Content-Disposition'] = content
    return response
class delete_invoice(SuccessMessageMixin, DeleteView):
    model = Invoices
    template_name = "Invoices/invoices_confirm_delete.html"
    success_url = reverse_lazy("invoices:list")
    success_message =  "Invoice was deleted successfully."
