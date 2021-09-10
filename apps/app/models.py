# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.utils.translation import activate



def get_enum_jugu(of='package_type'):
    if(of=='package_size'):
        return (
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
        )

    elif(of=='provider_type'):
        return (
            ('C', 'Company'),
            ('P', 'Person'),
            ('O', 'Other'),
        )

    elif(of=='gender_type'):
        return (
            ('M', 'Male'),
            ('F', 'Female'),
        )




# add timestamps for tables
class Extra_jugu(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        abstract = True


# add commun user info for tables
class Extra_UserProfile_Info_jugu(models.Model):
    phone_number = models.CharField(unique=True, blank=None, null=False, max_length=12)
    birthday = models.DateField(null=True, blank=True),
    #profile_img = models.ImageField(verbose_name='Profile Picture', upload_to = 'consumers/img/profile_img/')
    gender = models.CharField(max_length=1,  choices=get_enum_jugu('gender_type'))
    address = models.CharField(max_length=100, verbose_name='Address')
    #address_num = models.IntegerField( verbose_name='Address Number')
    city = models.CharField(max_length=40, verbose_name='City')
    state = models.CharField(max_length=40, verbose_name='State')
    zip = models.CharField(max_length=30, verbose_name='Zip Code')

    class Meta:
        abstract = True

########################## Tables ###########################
class Package_Type(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=None)

    def __str__(self):
        return self.name+'_Package'

class Provider(Extra_UserProfile_Info_jugu, Extra_jugu):
    name = models.CharField(max_length=100, unique=True, null=False, blank=None)
    email = models.EmailField(unique=True,  null=True, blank=False, default=None) 
    type = models.CharField(max_length=9, verbose_name='Provider type', choices=get_enum_jugu('provider_type'))
    profile_img = models.ImageField(verbose_name='Profile Picture', upload_to = 'provider/img/profile_img/')
    #created_by

    def __str__(self):
        return self.name+'_Package'


class User_Profile(Extra_UserProfile_Info_jugu):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone_number = models.CharField(unique=True, blank=None, null=False, max_length=12) 
    profile_img = models.ImageField(verbose_name='Profile Picture', upload_to = 'users/img/profile_img/')

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name+' ('+self.user.username+')'


class Package(Extra_jugu):
    provider = models.ForeignKey(Provider,on_delete=models.CASCADE,)
    size = models.CharField(max_length=1, verbose_name='Package size', choices=get_enum_jugu('package_type'))
    type = models.ForeignKey(Package_Type,on_delete=models.CASCADE, verbose_name='Package type')
    cost = models.DecimalField(max_digits=9, decimal_places=2, null=False, default=0.00)
    name = models.CharField( max_length=100, blank=False)
    available = models.IntegerField( verbose_name='Available packages', default=0)


    def __str__(self):
        return self.name+' : '+self.type.name+' by ( '+self.provider.name+' )'

    class Meta:
        pass
        #ordering = ['headline']


# Create your models here.
class Consumer(Extra_jugu, Extra_UserProfile_Info_jugu):
    
    first_name = models.CharField( max_length=30, blank=None, null=False)
    last_name = models.CharField(max_length=30, blank=None, null=False)
    email = models.EmailField(unique=True,  null=True)
    id_card_img = models.ImageField(verbose_name='Identity Card Image')
    num_wives = models.IntegerField( verbose_name='Number of wives', default=0)
    num_children = models.IntegerField( verbose_name='Number of Children', default=0)
    id_card_num = models.IntegerField( unique=True, null=False)
    num_packages = models.IntegerField( unique=True, null=False, verbose_name='Number of packages received')
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    provided_at = models.DateTimeField(default=datetime.now)
    priority = models.IntegerField(verbose_name='Priority', default=1)
    profile_img = models.ImageField(verbose_name='Profile Picture', upload_to = 'consumers/img/profile_img/')

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
