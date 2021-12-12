# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Jugurtha-Green
"""

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# add timestamps for tables


def get_enum_jugu(of='package_type'):
    if(of == 'gender_type'):
        return (
            ('M', 'Male'),
            ('F', 'Female'),
        )


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile', null=False, blank=False)
    profile_img = models.ImageField( verbose_name='Profile Picture', upload_to='users/img/profile_img/', null=True, blank=True)
    profile_img = models.ImageField(verbose_name='Cover Picture', upload_to='users/img/cover_img/', null=True, blank=True)
    phone_number = models.CharField(unique=True, blank=None, null=False, max_length=12)
    birthday = models.DateField(null=True, blank=True)
    #profile_img = models.ImageField(verbose_name='Profile Picture', upload_to = 'consumers/img/profile_img/')
    gender = models.SlugField( max_length=1,  choices=get_enum_jugu('gender_type'))
    address = models.CharField(max_length=100, verbose_name='Address')
    #address_num = models.IntegerField( verbose_name='Address Number')
    city = models.CharField(null=True, blank=True, max_length=40, verbose_name='City')
    state = models.CharField(null=True, blank=True, max_length=40, verbose_name='State')
    zip = models.CharField(null=True, blank=True, max_length=30, verbose_name='Zip Code')

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name+' ('+self.user.username+')'
