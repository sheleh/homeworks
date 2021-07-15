from django.forms import ModelForm
from .models import Users, Groups


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'is_admin', 'group']


class GroupForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['group_name', 'group_description']