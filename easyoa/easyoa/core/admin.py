# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

class BaseAdmin(admin.ModelAdmin):
    list_display = ('id','code','name','createdate','modifydate','author')
    search_fields =('code','name',)
    ordering = ('-id',)
    date_hierarchy = 'modifydate'
    save_on_top = True
    readonly_fields=('createdate','modifydate','author')
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

