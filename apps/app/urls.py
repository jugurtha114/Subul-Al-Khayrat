# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Jugurtha-Green
"""

from django.urls import path, re_path
from apps.app import views


app_name = "app"

urlpatterns = [

    # The home page
    path('dashboard/', views.dashboard, name='dashboard'),
    path('consumers/', views.Consumer_ListView.as_view(), name='consumer_list'),

    path('consumers/<int:pk>/edit/', views.ConsumerUpdateView.as_view(), name='consumer_edit'),
    path('consumers/<int:pk>/delete/', views.ConsumerDeleteView.as_view(), name='consumer_delete'),
    path('consumers/<int:pk>/', views.consumer_form, name='consumer_details'),
    path('consumers/new/', views.ConsumerCreateView.as_view(), name='consumer_new'),
    path('consumers_autocomplete/', views.ConsumerAutocomplete.as_view(), name='consumer_autocomplete',),
    path('general_search/', views.ConsumerAutocomplete.as_view(), name='general_search_autocomplete',),
 
    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

]
