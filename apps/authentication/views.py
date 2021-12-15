# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Jugurtha-Green
"""
import hashlib

# Create your views here.
from django.db.models.fields import NOT_PROVIDED
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.translation import npgettext
from .forms import LoginForm, SignUpForm, UserProfile_Form, EditUser_Form
from django.urls import reverse

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse, reverse_lazy
#from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView,  DetailView, DeleteView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
#from .backend.models_jugu import *
from .models import User_Profile



class LockedView(TemplateView):
    template_name = 'accounts/locked.html'

    def get(self, request):
        activation_code = request.GET.get('code')
        if activation_code:
            salt = f'{request.user.username}-jugu'
            if activation_code == hash(salt):
                u = User_Profile.objects.filter(pk=request.user.id)
                u.is_verified = True
                u.save(update_fields=["is_verified"])
                return HttpResponseRedirect(reverse_lazy('app:consumer_list'))
            else:
                msg = 'Invalid Activation Code!!!'
                return render(request, self.template_name, {"msg": msg})
        return render(request, self.template_name)


def User_ProfileUpdateView(request):
    #user = User.objects.select_related().get(pk=request.user.id)
    context ={'segment':'settings'}
    if request.method == 'POST':
        form = EditUser_Form(request.POST or None, instance=request.user)
        form1 = UserProfile_Form(request.POST or None, request.FILES or None, instance=request.user.user_profile)
        
        if form.is_valid() and form1.is_valid():
          form.save()
          form1.save()
          return HttpResponseRedirect(reverse_lazy('account:settings'))
        else:
            msg = 'Error validating the form'
            args = {'form': form, 'form1': form1, }
            return render(request, "accounts/settings.html", {"msg": msg, **args, **context})
    else:
        form = EditUser_Form(instance=request.user)
        form1 = UserProfile_Form(instance=request.user.user_profile)
        
        args = {'form': form, 'form1': form1, **context}
        return render(request, 'accounts/settings.html', args)

# class User_ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     #model = User_Profile
#     form_class = User_ProfileForm
#     template_name = 'accounts/settings.html'
    
#     #queryset = User_Profile.objects.select_related()
#     #context_object_name = 'fd'
#     #pk_url_kwarg = 'pk'
#     fields = ['profile_img', 'gender', 'phone_number', 'birthday', 'address', 'zip', 'city', 'state',]
#     success_url = reverse_lazy('account:settings')
    
#     def get_queryset(self):
#         print('*'*20)
#         print(self.request.user.id)
#         print('*'*20)
#         return User_Profile.objects.select_related().filter(pk=self.request.user.id)
    

#     def get(self, request, *args: str, **kwargs) -> HttpResponse:
#         self.queryset = User_Profile.objects.select_related().filter(pk=request.user.id)

#         return super().get(request, *args, **kwargs)

# user.user_permissions.set([permission_list])
# user.user_permissions.add(permission, permission, ...)
# user.user_permissions.remove(permission, permission, ...)
# user.user_permissions.clear()


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if not user.is_active:
                    msg = 'User account is Disabled'
                else:
                    login(request, user)
                    print('[+] User : {user} logged in!')
                    return redirect(reverse('app:consumer_list'))
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.is_active = False
            form.save()
            u=form.instance          
            #print(f'creating pk= {u}')
            profile = User_Profile.objects.create(user=u, phone_number=form.cleaned_data['phone_number'], is_verified=False)
            profile.is_verified=False
            #profile.phone_number = form.cleaned_data['phone_number']
            # content_type = ContentType.objects.get_for_model(User)
            # permission = Permission.objects.get(codename='admin_can_manage_users')
            # user.user_permissions.add(permission)
            profile.save()

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)


            # user.user_permissions.set([permission_list])
            # user.user_permissions.add(permission, permission, ...)
            # user.user_permissions.remove(permission, permission, ...)
            # user.user_permissions.clear()

            # doctor_group.permissions.set([permission_list])
            # doctor_group.permissions.add(permission, permission, ...)
            # doctor_group.permissions.remove(permission, permission, ...)
            # doctor_group.permissions.clear()

            #user.groups.add(doctor_group)

            ######  Check user in the group
            # def is_doctor(user):
            #     return user.groups.filter(name='Doctor').exists()
            # from django.contrib.auth.decorators import user_passes_test
            # @user_passes_test(is_doctor)
            # def my_view(request):
            #     pass

            # user.user_permissions.clear()                    
            # user.user_permissions.set(['view_user_profile','change_user_profile',])

            if user is not None:
                success = True
                if not user.is_active:
                    msg = 'User account is Disabled'
                else:
                    login(request, user)
                    print('[+] User : {user} logged in!')
                    return HttpResponseRedirect(reverse_lazy('account:settings'))
                    return redirect(reverse('account:loggin'))
                    # msg = 'User created - please <a href="/login">login</a>.'
                    

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
