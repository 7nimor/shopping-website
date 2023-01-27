from django.db import models


# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='متن اسلایدر')
    url = models.CharField(max_length=200, verbose_name='لینک')
    url_title = models.CharField(max_length=200, verbose_name='متن لینک')
    slider_image = models.ImageField(upload_to='media/sliders', verbose_name='عکس اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال', null=True)

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title
