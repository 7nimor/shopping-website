# Generated by Django 4.1.4 on 2023-01-08 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articule_module', '0002_alter_articlecategory_url_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecategory',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articule_module.articlecategory', verbose_name='دسته بندی والد'),
        ),
    ]
