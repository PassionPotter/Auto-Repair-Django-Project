from . import views
from django.urls import path




app_name='InformacionTiendas'

urlpatterns=[
    path('',views.IndexClassView.as_view(),name='list_tiendas'),
    path('add',views.InformacionTiendasAdd.as_view(),name='create_tiendas'),
    path('edit/<int:pk>',views.EditClassView.as_view(),name='edit_tiendas'),
    path('<int:pk>/', views.tiendas_detail.as_view(), name='tiendas_detail'),
    path('delete/<int:pk>', views.eliminar_tiendas.as_view(), name='tiendas_delete'),
]