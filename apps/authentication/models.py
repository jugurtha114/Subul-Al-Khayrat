# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Jugurtha-Green
"""

from django.db import models
from django.contrib.auth.models import User, AbstractUser
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
    profile_img = models.ImageField(verbose_name='Profile Picture', upload_to='users/img/profile_img/', null=True, blank=True)
    cover_img = models.ImageField(verbose_name='Cover Picture', upload_to='users/img/cover_img/', null=True, blank=True)
    phone_number = models.CharField( blank=True, null=True, max_length=12)#unique=True,
    birthday = models.DateField(null=True, blank=True)
    #profile_img = models.ImageField(verbose_name='Profile Picture', upload_to = 'consumers/img/profile_img/')
    gender = models.SlugField( max_length=1,  choices=get_enum_jugu('gender_type'))
    address = models.CharField(max_length=100, verbose_name='Address')
    is_verified = models.BooleanField(verbose_name='Is Verified')
    city = models.CharField(null=True, blank=True, max_length=40, verbose_name='City')
    state = models.CharField(null=True, blank=True, max_length=40, verbose_name='State')
    zip = models.CharField(null=True, blank=True, max_length=30, verbose_name='Zip Code')

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name+' ('+self.user.username+')'
    # class Meta:
    #     permissions = (
    #         ("view_vote_office", "can view vote office"),
    #         ("find_vote", "can find vote"),
    #     )

    @property
    def get_profile_img_url(self):
        if self.profile_img and hasattr(self.profile_img, 'url'):
            return self.profile_img.url
        else:
            return 'https://cdn-icons-png.flaticon.com/512/149/149071.png'

    @property
    def get_cover_img_url(self):
        if self.cover_img and hasattr(self.cover_img, 'url'):
            return self.cover_img.url
        else:
            return 'https://scontent.faae2-2.fna.fbcdn.net/v/t1.6435-9/131664299_211394117180234_9160915970713720252_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=e3f864&_nc_eui2=AeGh-006M_Cw49ilYnbSZE2ExHAzLIAwk-fEcDMsgDCT535YhW9VXTIw-lOnSQi6sqontMR_BK2OE4IQWHNuBx3V&_nc_ohc=cWOeIR06BY0AX_JoAaF&_nc_ht=scontent.faae2-2.fna&oh=00_AT87kUHZ-sE4AfH2Z3dXS5Cy6QaYHh8xsplTpsQAnCh_TA&oe=61DF1E7C'

    # @property
    # def get_photo_url(self):
    #     if self.photo and hasattr(self.photo, 'url'):
    #         return self.photo.url
    #     else:
    #         return "/static/images/user.jpg"
