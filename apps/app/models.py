# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.utils.translation import activate
from django.utils import timezone



def get_enum_jugu(of='package_type'):
    if(of=='package_size'):
        return (
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
            ('X', 'Extra Large'),
        )

    elif(of=='provider_type'):
        return (
            ('C', 'Company'),
            ('P', 'Person'),
            ('O', 'Other'),
        )
    
    elif(of=='subscription_status'):
        return (
            ('A', 'Active'),
            ('P', 'Pending'),
            ('S', 'Suspended'),
        )
    elif(of == 'gender_type'):
        return (
            ('M', 'Male'),
            ('F', 'Female'),
        )




# add timestamps for tables
class Extra_jugu(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False )

    class Meta:
        abstract = True


# class Extra_UserProfile_Info_jugu(models.Model):
#     post_code = models.CharField(max_length=40, verbose_name='Postal Code')
#     post_name = models.CharField(max_length=40, verbose_name='Postal Name AR')
#     post_name_ascii = models.CharField(max_length=40, verbose_name='Postal Name')
#     post_address = models.CharField(max_length=40, verbose_name='Postal Address AR')
#     post_address_ascii = models.CharField(max_length=40, verbose_name='Postal Address AR')
#     commune_id = models.CharField(max_length=40, verbose_name='City')
#     commune_name = models.CharField(max_length=40, verbose_name='City')
#     commune_name_ascii = models.CharField(max_length=40, verbose_name='City')
#     daira_name = models.CharField(max_length=40, verbose_name='Postal Code AR')
#     daira_name_ascii = models.CharField(max_length=40, verbose_name='Postal Code')
#     wilaya_code = models.CharField(max_length=40, verbose_name='State code')
#     wilaya_name = models.CharField(max_length=40, verbose_name='City')
#     wilaya_name_ascii = models.CharField(max_length=40, verbose_name='City')



# add commun user info for tables
class Extra_UserProfile_Info_jugu(models.Model):
    phone_number = models.CharField(unique=True, blank=None, null=False, max_length=12)
    birthday = models.DateField(null=True, blank=True)
    #profile_img = models.ImageField(verbose_name='Profile Picture', upload_to = 'consumers/img/profile_img/')
    gender = models.SlugField(max_length=1,  choices=get_enum_jugu('gender_type'))
    address = models.CharField(max_length=100, verbose_name='Address')
    #address_num = models.IntegerField( verbose_name='Address Number')
    city = models.CharField(null=True, blank=True, max_length=40, verbose_name='City')
    state = models.CharField(null=True, blank=True, max_length=40, verbose_name='State')
    zip = models.CharField(null=True, blank=True, max_length=30, verbose_name='Zip Code')

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




class Package(Extra_jugu):
    provider = models.ForeignKey(Provider,on_delete=models.CASCADE,)
    size = models.SlugField( max_length=1, verbose_name='Package size', choices=get_enum_jugu('package_type'))
    type = models.ForeignKey(Package_Type,on_delete=models.CASCADE, verbose_name='Package type')
    cost = models.DecimalField(max_digits=9, decimal_places=2, null=False, default=0.00)
    name = models.CharField( max_length=100, blank=False)
    available = models.IntegerField( verbose_name='Available packages', default=0)


    def __str__(self):
        return self.name+' : '+self.type.name+' by ( '+self.provider.name+' )'

    class Meta:
        pass
        #ordering = ['headline']


class Consumer(Extra_jugu, Extra_UserProfile_Info_jugu):
 
    first_name = models.CharField(max_length=30, blank=None, null=False)
    last_name = models.CharField(max_length=30, blank=None, null=False)
    email = models.EmailField(unique=True,  null=True)#
    id_card_img = models.ImageField(verbose_name='Identity Card Image')
    num_wives = models.IntegerField(verbose_name='Number of wives', default=0)
    num_children = models.PositiveSmallIntegerField(verbose_name='Number of Children', default=0)
    id_card_num = models.IntegerField(unique=True, null=False)
    num_packages = models.IntegerField(default=1,  null=False, verbose_name='Number of packages received')
    package = models.ForeignKey( Package, on_delete=models.DO_NOTHING,  null=True)
    provided_at = models.DateTimeField(default=datetime.now)
    priority = models.PositiveSmallIntegerField( verbose_name='Priority', default=1)
    profile_img = models.ImageField(verbose_name='Profile Picture', blank=True, null=True, upload_to='consumers/img/profile_img/')
    subscription_status = models.SlugField(max_length=1, verbose_name='Subscription Status', choices=get_enum_jugu('subscription_status'))
    is_responsable = models.BooleanField(null=False, blank=False)
    description = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Description')
    family = models.ForeignKey('self', on_delete=models.DO_NOTHING,null=True, blank=True,  verbose_name='Responsable')

    def __str__(self):
        is_res = ''
        if self.is_responsable:
            is_res = ' (Responsable)'
        return "%s %s %s" % (self.first_name, self.last_name, is_res)

    @property
    def get_profile_img_url(self):
        if self.profile_img and hasattr(self.profile_img, 'url'):
            return self.profile_img.url
        else:
            return '/media/default/img/profile_img/1.png'

    @property
    def get_dict_jugu(self):
        data_dict = {}

        data_dict['name'] = f'{self.first_name} {self.last_name}'
        data_dict['wives_children'] = str(self.num_wives)+' ( '+ str(self.num_children)+' )'
        data_dict['state_city'] = f'{self.state}, {self.city}'
        return data_dict

    @property
    def is_providable(self):
        return ((timezone.now() - self.provided_at).total_seconds() > 864000)



    class Meta:
        ordering = ["-provided_at"]

    def get_fields_jugu(self):
        # list of some excluded fields
        excluded_fields = ['id', 'pk']

        # getting all fields that available in `Consumer` model,
        # but not in `excluded_fields`
        field_names = [field.name for field in Consumer._meta.get_fields() 
                       if field.name not in excluded_fields]

        return field_names
        values = []
        for field_name in field_names:
            # get specific value from instanced object.
            # and outputing as `string` value.
            values.append('%s' % getattr(self, field_name))

        # joining all string values.
        return ' | '.join(values)


# class Family(Extra_jugu):
#     has_house = models.BooleanField(null=True, blank=True, default=True)
#     members = models.IntegerField(verbose_name='Family members')

    # def __str__(self):
    #     return f'{self.responsable.last_name} Family'
