"""assignment_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users_roles import views

urlpatterns = [
    path('admin/', admin.site.urls, name='users'),
    # Users
    path('', views.all_users),
    path('all_users', views.all_users, name='all_users'),
    path('create_user', views.create_user, name='create_user'),
    path('edit_user/<int:user_pk>', views.edit_user, name='edit_user'),
    path('user/<int:user_pk>/delete', views.delete_user, name='delete_user'),
    # Group
    path('all_groups', views.all_groups, name='all_groups'),
    path('create_group', views.create_group, name='create_group'),
    path('edit_group/<int:group_pk>', views.edit_group, name='edit_group'),
    path('group/<int:group_pk>/delete', views.delete_group, name='delete_group'),
]
