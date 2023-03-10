# Generated by Django 4.1.4 on 2023-01-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='متن اسلایدر')),
                ('url', models.CharField(max_length=200, verbose_name='لینک')),
                ('url_title', models.CharField(max_length=200, verbose_name='متن لینک')),
                ('slider_image', models.ImageField(upload_to='media/sliders', verbose_name='عکس اسلایدر')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدرها',
            },
        ),
    ]
