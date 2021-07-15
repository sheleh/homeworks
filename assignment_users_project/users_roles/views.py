from django.shortcuts import render, get_object_or_404, redirect
from .models import Users, Groups
from .forms import UserForm, GroupForm


def all_users(request):
    users = Users.objects.all()
    return render(request, 'users_roles/all_users.html', {'users': users})


def create_user(request):
    if request.method == 'GET':
        select_groups = Groups.objects.all()
        return render(request, 'users_roles/create_user.html', {'form': UserForm(), 'select_groups': select_groups})
    else:
        try:
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(all_users)
            else:
                return render(request, 'users_roles/create_user.html', {'form': UserForm(), 'error': form.errors})
        except ValueError:
            return render(request, 'users_roles/create_user.html', {'form': UserForm(), 'error': 'Bad data'})


def edit_user(request, user_pk):
    user = get_object_or_404(Users, pk=user_pk)
    if request.method == 'GET':
        form = UserForm(instance=user)
        return render(request, 'users_roles/edit_user.html', {'user': user, 'form': form})
    else:
        try:
            form = UserForm(request.POST, instance=user)
            form.save()
            return redirect(all_users)
        except ValueError:
            return render(request, 'users_roles/edit_user.html', {'error': 'Bad data'})


def delete_user(request, user_pk):
    user = get_object_or_404(Users, pk=user_pk)
    if request.method == 'POST':
        try:
            user.delete()
        finally:
            return redirect('all_users')


def all_groups(request):
    groups = Groups.objects.all()
    return render(request, 'users_roles/all_groups.html', {'groups': groups})


def create_group(request):
    if request.method == 'GET':
        return render(request, 'users_roles/create_group.html', {'form': GroupForm()})
    else:
        try:
            form = GroupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(all_groups)
            else:
                return render(request, 'users_roles/create_group.html', {'form': GroupForm(), 'error': form.errors})
        except ValueError:
            return render(request, 'users_roles/create_group.html', {'form': GroupForm(), 'error': 'Bad data'})


def edit_group(request, group_pk):
    group = get_object_or_404(Groups, pk=group_pk)
    if request.method == 'GET':
        form = GroupForm(instance=group)
        return render(request, 'users_roles/edit_group.html', {'group': group, 'form': form})
    else:
        try:
            form = GroupForm(request.POST, instance=group)
            form.save()
            return redirect(all_groups)
        except ValueError:
            return render(request, 'users_roles/edit_group.html', {'error': 'Bad data'})


def delete_group(request, group_pk):
    group = get_object_or_404(Groups, pk=group_pk)
    if request.method == 'POST':
        try:
            group.delete()
        finally:
            return redirect('all_groups')