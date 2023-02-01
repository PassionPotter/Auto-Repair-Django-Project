from . import views
from django.urls import path

app_name='Presupuestos'

urlpatterns=[
    # path('new-customer',views.create_Presupuestos,name='nuevo-presupuestos'),
    path('step1',views.step1,name='step1'),
    path('step2',views.step2,name='step2'),
    path('step3',views.step3,name='step3'),
    path('step4',views.step4,name='step4'),
    path('step5',views.step5,name='step5'),
    path('step6',views.step6,name='step6'),
    path('step7/',views.step7,name='step7'),
    path('step8',views.step8,name='step8'),
    path('',views.presupuestosIndex,name='presupuestos'),
    path('add-pay/<int:pk>',views.addPay,name='add-pay'),
    path('add-part/<int:pk>',views.addPart,name='add-part'),
    path('add-labor/<int:pk>',views.addLabor,name='add-labor'),
    path('detail/<int:pk>', views.detail_presupuestos, name='detail'),
    path('cancel/<int:pk>', views.cancel_presupuestos, name='cancel-estimate'),
    path('download-pdf/<int:pk>', views.download_pdf, name='download-estimate'),
    path('detail-in-pdf/<int:pk>', views.detail_in_pdf, name='detail-in-pdf'),
]

