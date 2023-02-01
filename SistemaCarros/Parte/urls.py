from . import views
from django.urls import path

app_name='parte'

urlpatterns=[
    path('',views.list_parte,name='list_parte'),
    path('add',views.create_parte.as_view(),name='add_parte'),
    path('edit/<int:pk>', views.edit_parte.as_view(), name='edit_parte'),
    path('delete/<int:pk>', views.eliminar_parte.as_view(), name='eliminar_parte'),
    path('<int:pk>/', views.detail_parte.as_view(), name='parte_detail'),
]
