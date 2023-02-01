from . import views
from django.urls import path

app_name='Pagos'

urlpatterns=[
    path('add',views.create_Pagos,name='pagos')
]
