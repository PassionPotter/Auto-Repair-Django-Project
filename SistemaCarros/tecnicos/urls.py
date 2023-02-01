from . import views
from django.urls import path

app_name='tecnicos'

urlpatterns=[
    path('',views.tecnico_list,name='list_tecnicos'),
    path('add',views.addTecnico.as_view(),name='add_tecnicos'),
    path('edit/<int:pk>', views.edit_inventory.as_view(), name='edit_tecnicos'),
    path('delete/<int:pk>', views.eliminar_tecnicos.as_view(), name='eliminar_tecnicos'),
    path('<int:pk>/', views.tecnicos_detail.as_view(), name='tecnicos_detail'),
    # path('edit',views.addPart.as_view(),name='add-part'),

]