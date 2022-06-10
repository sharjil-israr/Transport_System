from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button
from django.forms import ModelForm
from accounts_engine.models import *
from django.urls import reverse

class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['email']


class UserDetailForm(forms.ModelForm):
    
    class Meta:
        model=UserDetail
        fields=('user','first_name','last_name','mobile','company','role','group','custom_permission',)
        widgets={
            'user':forms.TextInput(attrs={'type':'hidden'}),            
            'company':forms.TextInput(attrs={'type':'hidden'}),
            'role':forms.SelectMultiple(attrs={'class': 'selectpicker multiple', 'data-style': 'select-with-transition', 'multiple': '',  'data-style': 'btn btn-primary', 'title': 'select role'}),
            'group':forms.SelectMultiple(attrs={'class': 'selectpicker multiple', 'data-style': 'select-with-transition', 'multiple': '',  'data-style': 'btn btn-primary', 'title': 'select group'}),
            'custom_permission' :forms.SelectMultiple(attrs={'class': 'selectpicker multiple', 'data-style': 'select-with-transition', 'multiple': '',  'data-style': 'btn btn-primary', 'title': 'select custom permission'}),
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method='POST'
        self.helper.add_input(Submit('add_user_details','Add'))        
        self.helperhelper.layout=Layout(
            Row(
                Column('first_name'),
                Column('last_name'),
                Column('mobile'),
            ),
            Row(
                Column('role'),                
            ),
            Row(
                Column('group'),
            ),
            Row(
                Column('custom_permission'),
            ),
            Row(
                Column('user'),
                Column('company'),
            )
        )        
        

class TaskForm(forms.ModelForm):

    class Meta:
        model=Task
        # fields=('task','description','task_for_user','end_date','status','created_by',)
        fields='__all__'
        widgets = {
            'created_by' : forms.TextInput(attrs={'type': 'hidden'}),
            'task_for_user' : forms.Select(attrs={'class': 'selectpicker', 'data-style': 'select-with-transition', 'data-style': 'btn btn-primary', 'title': 'select User'}),
            'end_date' : forms.DateInput(attrs={'type': 'date', 'class': 'mt-5'}),

        }
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method='post'
        self.helper.add_input(Submit('add_Task', 'Add'))
        self.helper.layout=Layout(
            Row(
                Column('Task'),                        
                ),
            Row(
                Column('description'),
                ),
            Row(
                Column('task_for_user'),
                Column('end_date'),
                ),                   
            Row(
                Column('created_by'),                      
                ),                    
            )


class PermissionForm(forms.ModelForm):
    class Meta:
        model= Permission
        fields=('section','url_name',)
        widgets={
                'section': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'select-with-transition', 'data-style': 'btn btn-primary', 'title': 'Select section'}),
                'url_name': forms.TextInput(attrs={'class':'mt-3'}),                
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.fields['section'].label='Section'
        self.fields['url_name'].label='URL Name'        
        self.helper.form_method='POST'
        self.helper.form_action=reverse('permission')
        self.helper.add_input(Submit('add_Permission','Add'))
        self.helper.layout=Layout(
                Row(
                    Column('section'),
                ),
                Row(
                    Column('url_name'),
                ),                

        )
        

class RoleForm(forms.ModelForm):

    class Meta:
        model=Role
        fields= ('role',)
        widgets={
            'role' : forms.TextInput()
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.fields['role'].label = "Role"
        self.helper.form_action=reverse('role')
        self.helper.add_input(Submit('Add_role','Add'))
        self.helper.layout=Layout(
            Row(
                Column('role'),
            )
        )


class GroupForm(forms.ModelForm):
    
    class Meta:
        model = Group
        fields ='__all__'
        Widgets = {
            'group': forms.TextInput()
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method ='POST'
        self.fields['group'].label = 'Group'        
        self.helper.form_action = reverse('group')
        self.helper.add_input(Submit('Add Group','Add'))
        self.helper.layout = Layout(
            Row(
                Column('group'),
            )
        )
        

class RoleWisePermissionForm(forms.ModelForm):

    class Meta:
        model=RoleWisePermission
        fields=('role','permission')
        widgets={
            'role': forms.TextInput(attrs={'type':'hidden'}),
            'permission':forms.SelectMultiple(attrs={'class':'selectpicker multiple','data-style':'select-with-transition','data-style':'btn btn-primary','title':'Select permission'})
        }


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method='POST'
        self.helper.add_input(Submit('Add Permission','Add'))
        self.helper.layout=Layout(
            Row(                
                Column('permission'),
            ),
            Row(
                Column('role')
            )
        )



class GroupWisePermissionForm(forms.ModelForm):

    class Meta:
        model=GroupWisePermission
        fields=('group','permission')
        widgets={
            'permission': forms.SelectMultiple(attrs={'class':'selectpicker multiple','data-style':'select-with-transition','data-style':'btn btn-primary','title':'Select group'}),
            'group':forms.TextInput(attrs={'type':'hidden'})
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('Add Permission','Add'))
        self.helper.layout=Layout(
            Row(
                Column('permission')
            ),
            Row(
                Column('group')
            )
        )