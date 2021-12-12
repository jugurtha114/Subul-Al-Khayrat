# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Jugurtha-Green
"""

# Create your views here.
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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


def User_ProfileUpdateView(request):
    #user = User.objects.select_related().get(pk=request.user.id)
    if request.method == 'POST':
        form = EditUser_Form(request.POST, instance=request.user)
        form1 = UserProfile_Form(request.POST, request.FILES, instance=request.user.user_profile)
        
        if form.is_valid and form1.is_valid:
          form.save()
          form1.save()
          return HttpResponseRedirect(reverse_lazy('account:settings'))
    else:
        form = EditUser_Form(instance=request.user)
        form1 = UserProfile_Form(instance=request.user.user_profile)
        
        args = { 'form': form, 'form1': form1,}
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
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
