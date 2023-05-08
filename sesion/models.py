from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

class Usuario(AbstractUser):
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',  # Cambia 'custom_user_set' por el nombre que prefieras
        help_text='The permissions this user has',
        related_query_name='user',
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',  # Cambia 'custom_user_set' por el nombre que prefieras
        help_text='The groups this user belongs to',
        related_query_name='user',
    )
    pass

# Create your models here.
