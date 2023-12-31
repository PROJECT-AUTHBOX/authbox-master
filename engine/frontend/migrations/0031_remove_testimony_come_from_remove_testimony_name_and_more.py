# Generated by Django 4.2.4 on 2023-08-24 10:41

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0030_testimony_testimonytranslation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimony',
            name='come_from',
        ),
        migrations.RemoveField(
            model_name='testimony',
            name='name',
        ),
        migrations.AddField(
            model_name='testimony',
            name='subtitle',
            field=django_cryptography.fields.encrypt(models.CharField(default=None, max_length=100, verbose_name='subtitle')),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimony',
            name='title',
            field=django_cryptography.fields.encrypt(models.CharField(default=None, max_length=100, verbose_name='title')),
            preserve_default=False,
        ),
    ]
