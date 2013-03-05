# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.utils import simplejson
from .models import *
from .forms import *
from easyoa.core.views import json,query
import xml.dom.minidom  
from easyoa.settings import HERE

def index(request):
    return render_to_response('index.html')

def getAccordionItem(request):
    doc = xml.dom.minidom.parse(HERE+'/oa/modules.xml')  
    data=[dict(node.attributes.items()) for node in doc.getElementsByTagName("sub_system")]
    return HttpResponse(simplejson.dumps(data))

def getAllTreeNode(request,parentId):
    doc = xml.dom.minidom.parse(HERE+'/oa/modules.xml')  
    node = doc.getElementById(parentId)
    data=[dict(zip(['pid','id','text','iconCls','attributes'], [m.parentNode.getAttribute('id'),m.getAttribute('id'), \
         m.getAttribute('text'),m.getAttribute('iconCls'),{'url':m.getAttribute('url')}])) \
         for m in node.getElementsByTagName("module")]
    return HttpResponse(simplejson.dumps(data))

def department(request):
    return render_to_response('department.html')
        
def departmentAction(request,action):
    if action=='query': return render_to_response('department_query.html')
    if action=='find':
        data=query(Department,request,{'name':'departmentName'})
        return HttpResponse(simplejson.dumps(data))
    if action=='add':
        form = DepartmentForm(request.POST or None)
        url = '/department/add'
        if request.method == "POST":
            if form.is_valid():
                o=form.save()
                data={'success':True,'msg':"成功增加一笔部门资料。",'obj':json(o),'isAdd':True}
                return HttpResponse(simplejson.dumps(data))
        t = get_template('department_pop.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))
    if action=='del':
        ids=request.GET['ids']
        for pk in ids.split(","):
            Department.objects.get(pk=pk).delete()
        data={'success':True,'msg':"成功删除部门资料。",'obj':None}
        return HttpResponse(simplejson.dumps(data))
    if action.startswith('edit')>0: 
        pk=action.split("/")[-1]
        instance = Department.objects.get(pk=pk)
        form = DepartmentForm(request.POST or None, instance = instance) 
        url = '/department/edit/'+pk
        if request.method == "POST":
            if form.is_valid():
                o=form.save()
                data={'success':True,'msg':"成功修改一笔部门资料。",'obj':json(o),'isAdd':False}
                return HttpResponse(simplejson.dumps(data))
        t = get_template('department_pop.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))       

def aclUser(request):
    return render_to_response('aclUser.html')
        
def aclUserAction(request,action):
    if action=='find':
        data=query(AclUser,request,{'name':'userName'})
        return HttpResponse(simplejson.dumps(data))
    if action=='add':
        form = AclUserForm(request.POST or None)
        url = '/aclUser/add'
        if request.method == "POST":
            if form.is_valid():
                o=form.save()
                data={'success':True,'msg':"成功增加一笔用户资料。",'obj':json(o),'isAdd':True}
                return HttpResponse(simplejson.dumps(data))
        t = get_template('aclUser_pop.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))
    if action=='del':
        ids=request.GET['ids']
        for pk in ids.split(","):
            AclUser.objects.get(pk=pk).delete()
        data={'success':True,'msg':"成功删除用户资料。",'obj':None}
        return HttpResponse(simplejson.dumps(data))
    if action.startswith('edit')>0: 
        pk=action.split("/")[-1]
        instance = AclUser.objects.get(pk=pk)
        form = AclUserForm(request.POST or None, instance = instance) 
        url = '/aclUser/edit/'+pk
        if request.method == "POST":
            if form.is_valid():
                o=form.save()
                data={'success':True,'msg':"成功修改一笔用户资料。",'obj':json(o),'isAdd':False}
                return HttpResponse(simplejson.dumps(data))
        t = get_template('aclUser_pop.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))       

