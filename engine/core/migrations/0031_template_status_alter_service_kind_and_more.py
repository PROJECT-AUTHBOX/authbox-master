# Generated by Django 4.2.4 on 2023-08-16 15:03

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_alter_agencytranslation_notes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=1),
        ),
        migrations.AlterField(
            model_name='service',
            name='kind',
            field=models.SmallIntegerField(choices=[(1, 'E-Commerce'), (2, 'Agency'), (3, 'Saas'), (4, 'Business'), (5, 'Portofolio'), (6, 'Blog'), (9, 'Other')]),
        ),
        migrations.AlterField(
            model_name='template',
            name='service_option',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'E-Commerce'), (2, 'Agency'), (3, 'Saas'), (4, 'Business'), (5, 'Portofolio'), (6, 'Blog'), (9, 'Other')], max_length=255, null=True),
        ),
    ]
