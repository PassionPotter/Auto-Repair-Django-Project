from django.contrib.auth.forms import UserChangeForm
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


COUNTRIES=(
    ('EUA', ('EUA')),
    ('Canada', ('Canada')),
    ('Other', ('Other')),
)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=0)
    image=models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    location=models.CharField(max_length=100,default=0)
    phone1=models.IntegerField(default=0)
    phone2=models.IntegerField(default=0)
    fax=models.IntegerField(default=0)
    email=models.CharField(max_length=100,default=0)
    website=models.CharField(max_length=100,default=0)
    socialMedia1=models.CharField(max_length=100,default=0)
    socialMedia2=models.CharField(max_length=100,default=0)
    socialMedia3 = models.CharField(max_length=100,default=0)
    alternativeContact=models.CharField(max_length=100,default=0)
    country = models.CharField(max_length=100, default=0,choices=COUNTRIES)
    address=models.CharField(max_length=100, default=0)
    city=models.CharField(max_length=100,default=0)
    state=models.CharField(max_length=100,default=0)
    zip=models.CharField(max_length=10,default=0)


    def __str__(self):
        return self.user.username





