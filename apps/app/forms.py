from django import forms
from dal import autocomplete
from .models import Consumer


# class MyForm(forms.Form):
#     media_type = forms.ChoiceField(
#         help_text="Select the order type.",
#         required=True,
#         label="Order Type:",
#         widget=RadioSelectButtonGroup,
#         choices=((1, 'Vinyl'), (2, 'Compact Disc')),
#         initial=1,
#     )
class GeneralSearchForm(forms.ModelForm):
    class Meta:
        widgets = {
            'general_search': autocomplete.ModelSelect2(
                url='app:general_search_autocomplete',
                attrs={'data-html': True},
                                                )
        }

class ConsumerForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ConsumerForm, self).__init__(*args, **kwargs)
    #     for name , field in self.fields.items():
    #         if field.widget.__class__ != forms.widgets.FileInput:
    #             if 'class' in field.widget.attrs:
    #                 field.widget.attrs['class'] += ' form-control'
    #             else:
    #                 field.widget.attrs.update({'class': 'form-control'})

    def save(self, user_jugu=None):
        if(not user_jugu):return super().save()
        obj = super().save(commit=False)
        obj.created_by = user_jugu
        obj.save()
        return obj

    def format_jugu(self, field=''):
        return "gggggggggg"

    class Meta:
        model = Consumer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'num_wives', 'num_children',
                  'id_card_num', 'subscription_status', 'num_packages', 'package', 'priority', 'profile_img', 
                  'gender', 'address', 'city', 'state', 'zip', 'is_responsable', 'description', 'family']
        exclude = ('created_by', 'created_at', 'updated_at', )
        widgets = {
            'family': autocomplete.ModelSelect2(url='app:consumer_autocomplete', 
            attrs={'data-html': True},
            )
        }




# first_name   = models.CharField(max_length=30, blank=None, null=False)
# last_name    = models.CharField(max_length=30, blank=None, null=False)
# email        = models.EmailField(unique=True,  null=True)
# id_card_img  = models.ImageField(verbose_name='Identity Card Image')
# num_wives    = models.IntegerField(verbose_name='Number of wives', default=0)
# num_children = models.IntegerField(verbose_name='Number of Children', default=0)
# id_card_num  = models.IntegerField(unique=True, null=False)
# num_packages = models.IntegerField(unique=True, null=False, verbose_name='Number of packages received')
# package      = models.ForeignKey(Package, on_delete=models.CASCADE)
# provided_at  = models.DateTimeField(default=datetime.now)
# priority     = models.IntegerField(verbose_name='Priority', default=1)
# profile_img  = models.ImageField(verbose_name='Profile Picture', upload_to='consumers/img/profile_img/')
# subscription_status = models.CharField( max_length=1, verbose_name='Subscription Status', choices=get_enum_jugu('subscription_status'))
# phone_number = models.CharField(unique=True, blank=None, null=False, max_length=12)
# birthday     = models.DateField(null=True, blank=True),
# #profile_img = models.ImageField(verbose_name='Profile Picture', upload_to = 'consumers/img/profile_img/')
# gender       = models.CharField(max_length=1,  choices=get_enum_jugu('gender_type'))
# address      = models.CharField(max_length=100, verbose_name='Address')
# #address_num = models.IntegerField( verbose_name='Address Number')
# city         = models.CharField(max_length=40, verbose_name='City')
# state        = models.CharField(max_length=40, verbose_name='State')
# zip          = models.CharField(max_length=30, verbose_name='Zip Code')

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "First Name",
    #             "class": "form-control"
    #         }
    #     ))

    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Last Name",
    #             "class": "form-control"
    #         }
    #     ))

    # birthday = forms.DateField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "dd/mm/yyyy",
    #             "class": "form-control",
    #             'data-datepicker':"",
    #         }
    #     ))

    # phone_number = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Last Name",
    #             "class": "form-control"
    #         }
    #     ))

    # subscription_status = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Subscription Status",
    #             "class": "form-control"
    #         }
    #     ))
    # email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "placeholder": "Email",
    #             "class": "form-control"
    #         }
    #     ))

    # id_card_num = forms.IntegerField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "ID Card Number",
    #             "class": "form-control"
    #         }
    #     ))

    # gender = forms.MultipleChoiceField(
    #     required=True,
    #     widget=forms.ChoiceField(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     ))

    # num_packages = forms.IntegerField(
    #     widget=forms.NumberInput(
    #         attrs={
    #             "placeholder": "Number of packages",
    #             "class": "form-control"
    #         }
    #     ))

    # address = forms.DateField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Address",
    #             "class": "form-control"
    #         }
    #     ))

    # city = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "City",
    #             "class": "form-control"
    #         }
    #     ))

    # zip = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "ZIP Code",
    #             "class": "form-control"
    #         }
    #     ))

    # state = forms.DateField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "State",
    #             "class": "form-control"
    #         }
    #     ))
