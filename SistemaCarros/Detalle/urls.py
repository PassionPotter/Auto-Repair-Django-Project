from . import views
from django.urls import path

app_name='Detalle'

urlpatterns=[
    path('add',views.create_Detalle,name='detalle')
]