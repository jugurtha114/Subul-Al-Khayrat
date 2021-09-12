# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Jugurtha-Green
"""

from django import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .backend.models_jugu import *
#from models import Consumer, Package, Package_Type,  Provider, User_Profile, User


#@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    #context['data_jugu'] = Context_jugu(page_name='index').get_context()
    #html_template = loader.get_template('index.html')
    #return HttpResponse(html_template.render(context, request))
    return render(request, 'index.html', context=context)



@login_required(login_url="/login/")
def consumers(request):
    context = {'segment': 'consumers'}
    context['data_jugu'] = Context_jugu(page_name='consumers').get_context()

    return render(request, 'consumers.html', context=context)

@login_required(login_url="/login/")
def dashboard(request):
    context = {'segment': 'consumers'}
    #context['data_jugu'] = Context_jugu(page_name='consumers').get_context()

    return render(request, 'dashboard.html', context=context)

'''

@login_required(login_url="/login/")
def pages(request):
    context = {}

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template in ['admin']:
            return HttpResponseRedirect(reverse('admin:index'))

        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        #return HttpResponse('Access forbidden by jugu!')
        #return render(request, 'dashboard.html', context=context)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        print('-'*130)
        print(e)
        print('-'*130)
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
'''

