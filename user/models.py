from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models


class MyUser(AbstractUser):
    
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='users', blank=True, null=True) 
    
    
   