import email
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomModel

# Create your models here.

class Custom(AbstractUser):
    username = None
    email = models.EmailField(_('emailaddress'),unique=True)
    mobile = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    last_logout = models.DateTimeField(null=True, blank=True)

    objects = CustomModel()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]



