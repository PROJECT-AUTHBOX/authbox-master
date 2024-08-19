# Generated by Django 4.2 on 2023-10-07 08:20

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_menudefault'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menudefault',
            name='service_option',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'E-Commerce'), (2, 'Agency'), (3, 'Saas'), (4, 'Business'), (5, 'Portofolio'), (6, 'Blog'), (7, 'Education'), (9, 'Other')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file_path',
            field=models.ImageField(blank=True, null=True, upload_to='temp'),
        ),
        migrations.AlterField(
            model_name='service',
            name='kind',
            field=models.SmallIntegerField(choices=[(1, 'E-Commerce'), (2, 'Agency'), (3, 'Saas'), (4, 'Business'), (5, 'Portofolio'), (6, 'Blog'), (7, 'Education'), (9, 'Other')]),
        ),
        migrations.AlterField(
            model_name='template',
            name='service_option',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'E-Commerce'), (2, 'Agency'), (3, 'Saas'), (4, 'Business'), (5, 'Portofolio'), (6, 'Blog'), (7, 'Education'), (9, 'Other')], max_length=255, null=True),
        ),
    ]