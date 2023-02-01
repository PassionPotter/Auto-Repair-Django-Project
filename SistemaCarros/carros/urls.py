from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from SistemaCarros import settings

# from django.conf import settings
from django.conf.urls.static import static


app_name='carros'

urlpatterns=[
    #/carros/
    path('',views.list_cars,name='list_cars'),
    path('add',views.create_carros.as_view(), name='create_carros'),
    path('addpicture',views.create_carros_picture, name='create_carros_picture'),
    path('addwarranty',views.create_carros_warranty, name='create_carros_warranty'),
    path('edit/<int:pk>',views.EditClassView.as_view(), name='edit_carros'),
    path('image_detail',views.Imagedetail, name='image_detail'),
    path('<int:pk>/',views.detail_carro.as_view(),name='detail_carro'),
    path('delete/<int:pk>',views.delete_carro.as_view(), name='eliminar_carros'),
    path('detail_invoice/<int:pk>', views.detail_invoices, name='detail_invoice'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        ) 
