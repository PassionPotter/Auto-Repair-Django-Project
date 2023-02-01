from . import views
from django.urls import path

app_name='ManoObra'

urlpatterns=[
    path('add',views.create_ManoObra,name='mano-obra') 
]
