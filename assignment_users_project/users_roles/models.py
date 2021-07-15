from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    group = models.ForeignKey('Groups', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.username


class Groups(models.Model):
    group_name = models.CharField(max_length=100)
    group_description = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name

