from django.db import models


class AdminUser(models.Model):

    a_username = models.CharField(max_length=16,unique=True)
    a_password = models.CharField(max_length=256)

