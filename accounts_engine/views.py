from itertools import count
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from pytest import Instance
from accounts_engine.decorators import is_user_allowed
from accounts_engine.forms import *
from .models import *
from django.contrib import messages


# Create your views here.
@login_required(login_url='/account/login/')
def dashboard(request):
    return render(request,'accounts_engine/dashboard.html')


@is_user_allowed
@login_required(login_url='/account/login/')
def my_profile(request):
    return render(request,'accounts_engine/my_profile.html')


# @is_user_allowed
# @login_required(login_url='/account/login/')
def view_profile(request,user_id):
    user_profile=CustomUser.objects.get(id=user_id)
    return render(request,'accounts_engine/my_profile.html',{
        'user_profile':user_profile
    })

@is_user_allowed
@login_required(login_url='/account/login/')
def tasks(request):
    task_list=Task.objects.filter(created_by = request.user) | Task.objects.filter(task_for_user = request.user)
    task_list.order_by('end_date')
    print(task_list)
    return render(request,'accounts_engine/tasks.html',{
        'task_list': task_list ,
        })

@is_user_allowed
@login_required(login_url='/account/login/')
def add_task(request):
    if request.method =='POST':
        task_form=TaskForm(request.POST,initial={'created_by':request.user})
        if task_form.is_valid():
            task_form.save
            messages.success(request,'Task successfully added..')
            return redirect('tasks')
    
    task_form=TaskForm( initial={'created_by': request.user})
    return render(request,'accounts_engine/add_task.html',{
                'task_form':task_form
            })



@is_user_allowed
@login_required(login_url='/account/login/')
def edit_task(request,task_id):
    pass


@is_user_allowed
@login_required(login_url='/account/login/')
def view_task(request,task_id):
    pass


@is_user_allowed
@login_required(login_url='/account/login/')
def delete_task(request,task_id):
    pass


@is_user_allowed
@login_required(login_url='/account/login/')
def update_status_task(request,task_id):
    pass


@is_user_allowed
@login_required(login_url='/account/login/')
def group(request):
    
    action_type = 'add'
    group_list = Group.objects.all()
    group_form = GroupForm()    
    if request.method == 'POST':
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group_form.save()
            messages.success(request,'New Group Added.')
            return redirect('group')
    
    return render(request,'accounts_engine/group.html',{
        'group_form': group_form,
        'group_list': group_list,
        'action_type': action_type
    })


@is_user_allowed
@login_required(login_url='/account/login/')
def group_edit(request,group_id):
    
    group_list=Group.objects.get(id=group_id)
    edit_group_form=GroupForm(instance=group_list)
    
    if request.method=='POST':
        edit_group_form=GroupForm(request.POST,instance=group_list)
        if edit_group_form.is_valid():
            edit_group_form.save()
            messages.warning(request,'Group updated.')
            return redirect('group')


    return render(request,'accounts_engine/group_edit.html',{
        'edit_group_form': edit_group_form,
        'group_id': group_id        
    })


@is_user_allowed
@login_required(login_url='/account/login/')
def group_delete(request,group_id):
    group=Group.objects.get(id=group_id)
    group_name=group.group
    group.delete()
    messages.error(request,'Group: ' + group_name + ' was deleted.')
    return redirect('group')


@is_user_allowed
@login_required(login_url='account/login')
def role(request):
    action_type = 'add'
    role_list = Role.objects.all()
    role_form = RoleForm()
    if request.method == 'POST':
        role_form=RoleForm(request.POST)
        if role_form.is_valid():
            role_form.save()
            messages.success(request,'New role created.')
            return redirect('role')

    return render(request,'accounts_engine/role.html',{
        'role_form':role_form,
        'role_list':role_list,
        'action_type':action_type
    })


@is_user_allowed
@login_required(login_url='account/login')
def role_edit(request,role_id):
   
    role=Role.objects.get(id=role_id)
    edit_role_form=RoleForm(instance=role)
    if request.method =='POST':
        edit_role_form=RoleForm(request.POST,instance=role)
        if edit_role_form.is_valid():
            role.save()
            messages.warning(request,'Role Upated.')
            return redirect('role')
   
   
    return render(request,'accounts_engine/role_edit.html',{
        'edit_role_form':edit_role_form,
        'role_id':role_id
    })


@is_user_allowed
@login_required(login_url='account/login')
def role_delete(request,role_id):
    role=Role.objects.get(id=role_id)
    role_name=role.role
    role.delete()
    messages.error(request,'Role: ' + role_name + ' was deleted.')
    return redirect('role')


@is_user_allowed
@login_required(login_url='/account/login/')
def permission(request):
    permission_form = PermissionForm()
    permission_list = Permission.objects.all()
    
    if request.method == 'POST':
        permission_form = PermissionForm(request.POST)
        if permission_form.is_valid():
            permission_form.save()
            messages.success(request, 'New permission created.')
            return redirect('permission')

    return render(request, 'accounts_engine/permission.html', {
        'permission_form': permission_form,
        'permission_list': permission_list,
    })


@is_user_allowed
@login_required(login_url='/account/login/')
def permission_edit(request,permission_id):
    permission=Permission.objects.get(id=permission_id)
    edit_permission_form=PermissionForm(instance=permission)

    if request.method == 'POST':
        edit_permission_form=PermissionForm(request.POST,instance=permission)
        if edit_permission_form.is_valid():
            edit_permission_form.save()
            messages.warning(request,'Permission Edited..')
            return redirect('permission')

    return render(request,'accounts_engine/permission_edit.html',{
        'edit_permission_form' : edit_permission_form,
        'permission_id':permission_id
    })


@is_user_allowed
@login_required(login_url='/account/login/')
def permission_delete(request,permission_id):
    permission = Permission.objects.get(id=permission_id)
    permission_name = permission.url_name
    permission.delete()
    messages.success(request,'Permission: ' + permission_name + 'was deleted.')
    return redirect('permission')


@is_user_allowed
@login_required(login_url='/account/login/')
def role_wise_permission(request,role_id):
   role=Role.objects.get(id=role_id)
   
   try:
        role_wise_permissions = RoleWisePermission.objects.get(role = role).permission.all()        
   except:
        role_wise_permissions=None
    
   if not role_wise_permissions or role_wise_permissions.count() == 0:        
        messages.error(request,'There are no permissions currently linked to this role. Please contact Admin')
        
   return render(request,'accounts_engine/role_wise_permission.html',{
        'role_wise_permissions': role_wise_permissions,
        'role': role
    })

@is_user_allowed
@login_required(login_url='/account/login/')
def add_permission_to_role(request,role_id):
    role=Role.objects.get(id=role_id)
        
    try:
        role_wise_permissions=RoleWisePermission.objects.get(role=role).permission.all()
        add_permission_to_role_form=RoleWisePermissionForm(instance=RoleWisePermission.objects.get(role = role))
    except:
        role_wise_permissions=None
        add_permission_to_role_form=RoleWisePermissionForm(initial={'role': role})
    
    if request.method == 'POST':
        if role_wise_permissions==None:
            add_permission_to_role_form=RoleWisePermissionForm(request.POST)
        else:    
            add_permission_to_role_form=RoleWisePermissionForm(request.POST,instance=RoleWisePermission.objects.get(role = role))
       
        if add_permission_to_role_form.is_valid():
            permission_to_role=add_permission_to_role_form.save(commit=False)
            permission_to_role.save()
            add_permission_to_role_form.save_m2m()
            messages.success(request,'New permission for role added.')
            return redirect('role_wise_permission',role_id)


    return render(request,'accounts_engine/role_wise_permission.html',{
        'add_permission_to_role_form':add_permission_to_role_form,
        'role_wise_permissions':role_wise_permissions,
         'role':role
    })


@is_user_allowed
@login_required(login_url='/account/login/')
def group_wise_permission(request,group_id):
    group=Group.objects.get(id=group_id)
    try:
        group_wise_permissions= GroupWisePermission.objects.get(group = group).permission.all()
    except:
        group_wise_permissions=None

    if not group_wise_permissions or group_wise_permissions.count() == 0 :
        messages.error(request,'No permission assossiated with this group.')        

    return render(request,'accounts_engine/group_wise_permission.html',{
        'group_wise_permissions': group_wise_permissions,
        'group': group
    })


@is_user_allowed
@login_required(login_url='/account/login/')
def add_permission_to_group(request,group_id):
    group=Group.objects.get(id=group_id)

    try:
        group_wise_permissions = GroupWisePermission.objects.get(group = group).permission.all()
        add_permission_to_group_form=GroupWisePermissionForm(instance=GroupWisePermission.objects.get(group = group))
    except:    
        group_wise_permissions=None
        add_permission_to_group_form=GroupWisePermissionForm(initial={'group':group})

    if request.method == 'POST':
        if group_wise_permissions==None:
            add_permission_to_group_form = GroupWisePermissionForm(request.POST)
        else:    
            add_permission_to_group_form = GroupWisePermissionForm(request.POST,instance=GroupWisePermission.objects.get(group = group))        

        if add_permission_to_group_form.is_valid():
            add_permission_to_group_form.save()
            messages.success(request,'New permisson added to group')
            return redirect('group_wise_permission', group_id)


    return render(request,'accounts_engine/group_wise_permission.html',{
        'add_permission_to_group_form': add_permission_to_group_form,
        'group_wise_permissions': group_wise_permissions,
        'group' : group
    })


@is_user_allowed
@login_required(login_url='/account/login/')
def remove_permission_to_role(request,role_id,permission_id):
    role=Role.objects.get(id=role_id)
    permission=Permission.objects.get(id=permission_id)
    role_wise_permission=RoleWisePermission.objects.get(role = role)
        
    msg ='Permission-' + permission + 'removed from role' + role + 'deleted..'
    role_wise_permission.remove(permission)
    messages.error(request,msg)
    return redirect('role_wise_permission')


@is_user_allowed
@login_required(login_url='/account/login/')
def remove_permission_to_group(request,group_id,permission_id):
    group=Group.objects.get(id=group_id)
    permission=Permission.objects.get(id=permission_id)
    group_wise_permission=GroupWisePermission.objects.get(permission=permission)
    group_wise_permission.delete(permission)
    msg='Permission- ' + 'removed for group ' + group
    messages.error(request,msg)
    return redirect('group_wise_permission')


@is_user_allowed
@login_required(login_url='/account/login/')
def users(request):
    user_list=UserDetail.objects.all()
    return render(request,'accounts_engine/users.html',{'user_list':user_list})    


@is_user_allowed
@login_required
def add_new_user(request):
    form=UserAdminCreationForm()
    if request.method =='POST':
        form=UserAdminCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            messages.success(request,'New User Created..')
            return redirect('add_user_details',new_user.id)    
        
    return render(request,'registration/add_new_user.html',{
            'form':form
        }) 



@is_user_allowed
@login_required   
def add_user_details(request,registered_user_id):
   
    registered_user=CustomUser.objects.get(id=registered_user_id) 
    company=request.user.get_user_detail().company
    add_user_detail_form=UserDetailForm(initial={'user': registered_user,'company':company})
   
    if request.method == 'POST':
        add_user_detail_form=UserDetailForm(request.post,request.user)
        if add_user_detail_form.is_valid():
            add_user_detail_form.save()
            messages.success(request,"User Added Sucessfully..")
            return redirect(request,'users/')    
        
    return render('accounts_engine/add_user_details.html',{
         'forms': UserDetail
       }) 

   
def edit_user_details(request,user_id):
    return render(request,'accounts_engine/users.html') 



def delete_user(request,user_id):
    return render(request,'accounts_engine/users.html') 
