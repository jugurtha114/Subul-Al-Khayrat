# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Jugurtha-Green
"""

from django.urls import path
from .views import login_view, register_user, User_ProfileUpdateView
from django.contrib.auth.views import LogoutView


#app_name='account'
app_name = 'account'

urlpatterns = [
    # {'pk': 1,}
    path('settings/', User_ProfileUpdateView, name="settings"),
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
    
]
