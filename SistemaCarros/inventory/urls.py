from . import views
from django.urls import path

app_name='inventory'

urlpatterns=[
    path('',views.list_inventory,name='list_inventory'),
    path('add',views.create_inventory.as_view(),name='add_inventory'),
    path('edit/<int:pk>', views.edit_inventory.as_view(), name='edit_inventory'),
    path('delete/<int:pk>', views.eliminar_inventory.as_view(), name='eliminar_inventory'),
    path('<int:pk>/', views.detail_inventory.as_view(), name='inventory_detail'),
]