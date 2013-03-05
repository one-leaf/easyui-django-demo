# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from easyoa.core.admin import BaseAdmin

class AclUserAdmin(BaseAdmin):
    list_display = ('id','code','name','department','birthday','createdate','modifydate','author')

admin.site.register(Department,BaseAdmin)
admin.site.register(AclUser,AclUserAdmin)

