# Generated by Django 4.2 on 2024-01-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_alter_agencymeta_image_type_alter_agencymeta_locale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencymeta',
            name='locale_alternate',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'id_ID'), (2, 'en_US')], default=2, verbose_name='locale alternate'),
        ),
        migrations.AlterField(
            model_name='agencymeta',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='site name'),
        ),
        migrations.AlterField(
            model_name='globalsetting',
            name='name',
            field=models.SmallIntegerField(choices=[(1, 'Slide Show'), (2, 'Menu'), (3, 'Why Us')], default=None),
        ),
    ]
