# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Jugurtha-Green
"""

from django.contrib import admin

from .models import Consumer, Package, Package_Type,  Provider
# Register your models here.

admin.site.register(Consumer)
admin.site.register(Package_Type)
admin.site.register(Package)
admin.site.register(Provider)

