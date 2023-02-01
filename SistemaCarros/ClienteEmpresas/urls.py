from . import views
from django.urls import path

app_name='ClienteEmpresas'

urlpatterns=[
    #/clienteEmpresas/
    #path('',views.IndexClassView.as_view(),name='index'),
    path('add', views.create_ClienteEmpresas, name='create_clienteempresas'),

]