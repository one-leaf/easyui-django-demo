# -*- coding: utf-8 -*-
from django.db import models
from easyoa.core.models import BaseModel

class Department(BaseModel):
    code=models.CharField(u'编码',max_length=100)
    name=models.CharField(u'名称',max_length=100)
    class Meta:
        verbose_name = u"部门"
        verbose_name_plural = u"部门"  

class AclUser(BaseModel):
    code=models.CharField(u'编码',max_length=100)
    name=models.CharField(u'名称',max_length=100)
    department=models.ForeignKey(Department,verbose_name=u'部门')
    birthday=models.DateField(u'生日',)
    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = u"用户"   

