# Generated by Django 4.2.4 on 2023-08-30 09:21

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0032_location_is_header_text_locationtranslation_subtitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagestranslation',
            name='sub_title',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=500, null=True, verbose_name='sub_title')),
        ),
    ]
