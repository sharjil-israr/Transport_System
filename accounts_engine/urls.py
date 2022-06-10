from django.urls import path
from django.urls import include
from . import views


urlpatterns=[
    path('',include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard ,name='dashboard'),
    
    path('profile/',views.my_profile,name='my_profile'),
    path('view_profile/<int:user_id>/',views.view_profile,name='view_profile'),

    path('tasks/',views.tasks,name='tasks'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:task_id>', views.edit_task , name = 'edit_task'),
    path('view_task/<int:task_id>', views.view_task ,name ='view_task'),
    path('delete_task/<int:task_id>', views.delete_task , name='delete_task'),
    path('update_status_task/<int:task_id>',views.update_status_task,name='update_status_task'),
            
    path('permission/',views.permission,name='permission'),
    path('permission/edit/<int:permission_id>',views.permission_edit,name='permission_edit'),
    path('permission/delete/<int:permission_id>',views.permission_delete,name='permission_delete'),    
    path('role-wise-permission/<int:role_id>',views.role_wise_permission,name='role_wise_permission'),   
    path('group-wise-permission/<int:group_id>',views.group_wise_permission,name='group_wise_permission'),
    path('add-permission-to-role/<int:role_id>',views.add_permission_to_role,name='add_permission_to_role'),
    path('add-permission-to-group/<int:group_id>',views.add_permission_to_group,name='add_permission_to_group'),
    path('remove-permission-to-role/<int:role_id>/<int:permission_id>',views.remove_permission_to_role,name='remove_permission_to_role'),
    path('remove-permission-to-group/<int:group_id>/<int:permission_id>',views.remove_permission_to_group,name='remove_permission_to_group'),

    path('role/',views.role,name='role'),
    path('role/edit/<int:role_id>',views.role_edit,name='role_edit'),
    path('role/delete/<int:role_id>',views.role_delete,name='role_delete'),

    path('group/',views.group,name='group'),
    path('group/edit/<int:group_id>',views.group_edit,name='group_edit'),
    path('group/delete/<int:group_id>',views.group_delete,name='group_delete'),



    path('users/',views.users,name='users'),
    path('add-new-user/',views.add_new_user,name='add_new_user'),
    path('add-user-details/<int:registered_user_id>/',views.add_user_details,name='add_user_details'),
    path('delete-user/<int:user_id>/',views.delete_user,name='delete_user'),
    path('edit-user-details/<int:user_id>/',views.edit_user_details,name='edit_user_details'),


]