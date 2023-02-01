
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegisterForm, PasswordChangingForm
from .models import Profile


def panel_admin(self):
    return redirect('panel_admin')

#registro
def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'Usuarios/registro.html', {'form': form})



#forgot password
class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request,'Usuarios/password_success.html',{})



@login_required
def profilepage(request):
    return render(request,'Usuarios/profile.html')



# class UserEditView(generic.UpdateView):
#     form_class=UserChangeForm
#     template_name='Usuarios/edit-profile.html'
#     success_url=reverse_lazy('profile')
#
#     def get_object(self):
#         return self.request.user


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'Usuarios/edit-profile.html'
    fields = ['user','location','phone1','phone2','fax','email','website','socialMedia1','socialMedia2',
              'socialMedia3','alternativeContact','country','address','city','state','zip']

