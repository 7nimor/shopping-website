from django.db import models


# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    text = models.TextField(verbose_name='متن پیام')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    response = models.TextField(verbose_name='متن پاسخ تماس با ما', null=True)

    class Meta:
        verbose_name = 'تماس با ما '
        verbose_name_plural = 'لیست تماس یا ما'

    def __str__(self):
        return self.title

