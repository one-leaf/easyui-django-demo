# -*- coding: utf-8 -*-

from django.db.models.query import QuerySet

def json(obj,fields=[]):
    if isinstance(obj,QuerySet):
        if fields==[]:
           return [dict(zip([f.name for f in o._meta.fields],[unicode(getattr(o,f.name)) for f in o._meta.fields])) for o in obj]
        return [dict(zip([f.name for f in fields],[unicode(getattr(o,f.name)) for f in fields])) for o in obj]
    else:
        if fields==[]:
           return dict(zip([f.name for f in obj._meta.fields],[unicode(getattr(obj,f.name)) for f in obj._meta.fields]))
        return dict(zip([f.name for f in fields],[unicode(getattr(obj,f.name)) for f in fields]))

def query(cls,request,queryDict):
    if request.GET.has_key('rows'):
        rows=int(request.GET['rows'])
        page=int(request.GET['page'])
    query={}
    for key in queryDict.keys():
        if request.GET.has_key(queryDict[key]):
            query['%s__contains'%key]=request.GET[queryDict[key]]
    total=cls.objects.filter(**query).count()
    if request.GET.has_key('rows'): 
        objs=cls.objects.filter(**query)[(page-1)*rows:page*rows]
    else: 
        objs=cls.objects.filter(**query)
    return {'total':total,'rows':json(objs)}

