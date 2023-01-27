from django.db import models

# Create your models here.
from account_module.models import User


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی مقالات'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=300, db_index=True, unique=True, verbose_name='عنوان در url')
    image = models.ImageField(upload_to='media/Article', verbose_name='عکس مقاله')
    short_description = models.CharField(max_length=200, verbose_name='توضیحات کوتاه')
    text = models.TextField(verbose_name='متن مقاله')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    select_category = models.ManyToManyField(ArticleCategory, verbose_name='دسته بندی ها')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', null=True, editable=False)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    parent = models.ForeignKey('ArticleComment', on_delete=models.CASCADE, verbose_name='والد', null=True,blank=True)
    text = models.TextField(verbose_name='متن نظر مقاله')

    class Meta:
        verbose_name = 'نظر مقاله'
        verbose_name_plural = 'نظرات مقاله'
