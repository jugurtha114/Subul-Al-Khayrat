# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Jugurtha-Green
"""

from django.urls import path, re_path
from apps.app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('consumers/', views.consumers, name='consumers'),
    #path('dashboard.html/', views.dashboard, name='dashboard'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
