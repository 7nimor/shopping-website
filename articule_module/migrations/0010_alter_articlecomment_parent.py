# Generated by Django 4.1.4 on 2023-01-09 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articule_module', '0009_alter_articlecomment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articule_module.articlecomment', verbose_name='والد'),
        ),
    ]