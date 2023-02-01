from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name='Foto'

urlpatterns=[
    path('add',views.create_Foto,name='foto')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)