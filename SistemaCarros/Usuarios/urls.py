from . import views
from django.urls import path

app_name='Usuarios'




urlpatterns=[
   path('profile',views.profilepage,name='profile'),

]