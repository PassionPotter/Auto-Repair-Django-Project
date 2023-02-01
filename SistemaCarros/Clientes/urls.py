from . import views
from django.urls import path
from django.conf.urls.i18n import i18n_patterns

app_name='Clientes'

urlpatterns=[
    path('',views.list_clientes,name='clientes_list'),
    path('add',views.create_clientes.as_view(),name='clientes_add'),
    path('edit/<int:pk>',views.edit_clientes.as_view(),name='clientes_edit'),
    path('<int:pk>/',views.detail_clientes.as_view(),name='clientes_detail'),
    path('delete/<int:pk>',views.eliminar_cliente.as_view(),name='clientes_delete'),
]

