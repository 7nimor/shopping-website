from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=200, verbose_name='موبایل')
    avatar = models.ImageField(upload_to='media/user', verbose_name='عکس کاربر', null=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل')
    about_user = models.CharField(max_length=200, verbose_name='توضیحات کاربر', null=True)
    address = models.TextField(verbose_name='آدرس', null=True, blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email
