# -*- coding: utf-8 -*-
from django.forms import CharField,FileField,TextInput,Textarea,ModelForm,Select
from .models import *

class DepartmentForm(ModelForm):
    class Meta:
        model = Department	
        exclude = ['createdate','modifydate','author']

class AclUserForm(ModelForm):
    class Meta:
        model = AclUser	
        exclude = ['createdate','modifydate','author']
        widgets = {
            'birthday': TextInput(attrs={'class': 'easyui-datebox',}),
            'department': Select(attrs={'class': 'easyui-combogrid','data-options': '''  
            	panelWidth: 500,
            	url: '/department/find',
            	idField: 'id',
            	textField: 'name',
            	mode: 'local',
            	fitColumns: true,
            	columns: [[
                    {field: 'id', title: 'Item ID', width: 60, checkbox: true},
                    {field: 'code', title: '部门编码', width: 80},
                    {field: 'name', title: '部门名称', align: 'right', width: 60}
                ]],
            	filter: function(q, row) {
                	return (row.code != null && row.code.indexOf(q) >= 0 || row.name != null && row.name.indexOf(q) >= 0);
            	}'''
            })
        }
