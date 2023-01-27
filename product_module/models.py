from django.db import models
from django.urls import reverse


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام برند')
    url_title = models.CharField(max_length=300, verbose_name='نام درurl ', db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(
        ProductCategory,
        related_name='product_categories',
        verbose_name='دسته بندی ها')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند محصول', null=True)
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to='upload', verbose_name='عکس محصول', null=True)
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.caption


class BannerModel(models.Model):
    class BannerPosition(models.TextChoices):
        product_list = ' product_list', 'صفحه لیست محصولات',
        product_detail = 'product_detail', 'صفحه جزییات محصولات',
        about_us = 'about_us', 'درباره ما'

    title = models.CharField(max_length=200, verbose_name='عنوان بنر')
    image = models.ImageField(verbose_name='عکس بنر', upload_to='media/banners')
    url = models.URLField(max_length=400, verbose_name='url بنر', null=True, blank=True)
    position = models.CharField(max_length=200, choices=BannerPosition.choices, verbose_name='محل قرار گیری بنر')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنر های تبلیغاتی'
