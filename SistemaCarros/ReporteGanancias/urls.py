from . import views
from django.urls import path,register_converter


app_name='ReporteGanancias'

class FloatUrlParameterConverter:
    regex = '[0-9]+\.?[0-9]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)
register_converter(FloatUrlParameterConverter, 'float')

urlpatterns=[
    path('',views.IndexReporteGanancias.as_view(),name='reporteganancias'),
    path('reports-debtors', views.reportsDebtors, name='debtors'),
    path('reports-pending-stock', views.pendingStock.as_view(), name='pending-stock'),
    path('reports-records', views.Records.as_view(), name='records'),
    path('reports-technicians', views.Technicians, name='technicians'),
    path('reports-workshops', views.Workshops, name='workshops'),
    path('reports-technicians-add-payment/<int:estimate>/<int:technico>', views.techniciansAddPayment, name='techniciansAddPayment'),
    path('reports-technicians-view-payment/<int:estimate>/<int:technico>/<float:percent>/<float:total>', views.techniciansViewPayment, name='techniciansViewPayment'),
    path('send-email/<int:pk>', views.send_email, name='send-email'),
    path('add-pay/<int:pk>',views.addPay,name='add-pay'),
    path('add-part/<int:pk>',views.addPart,name='add-part'),
    path('add-labor/<int:pk>',views.addLabor,name='add-labor'),
    path('detail-invoice/<int:pk>',views.ViewInvoice,name='detail-invoice'),
    path('reports-technicians-delete-payment/<int:id>', views.DeletePayment, name='technicianDeletePayment')
    # path('edit/<int:pk>', views.edit_inventory.as_view(), name='edit_tecnicos'),
    # path('edit',views.addPart.as_view(),name='add-part'),
] 
