from . import views
from django.urls import path

app_name='invoices'

urlpatterns=[
    path('',views.list_invoices.as_view(),name='list'),
    path('download-invoice/<int:pk>', views.download_pdf, name='download-invoice'),
    path('detail/<int:pk>', views.detail_invoices, name='detail'),
    path('eliminar_invoice/<int:pk>',views.delete_invoice.as_view(), name='eliminar_invoice'),
]