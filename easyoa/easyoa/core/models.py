# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    createdate=models.DateTimeField(u'创建时间',auto_now_add=True)
    modifydate=models.DateTimeField(u'更新时间',auto_now=True)
    author=models.ForeignKey(User,related_name='%(app_label)s_%(class)s_author_related',verbose_name=u'修改人',null=True)
    class Meta:
        abstract = True
    def __unicode__(self):
        if hasattr(self,'name'):
            return self.name
        else:
            return str(self.id)




