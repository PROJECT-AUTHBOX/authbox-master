# Generated by Django 4.1.2 on 2023-05-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_service_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='template',
        ),
        migrations.AddField(
            model_name='service',
            name='template',
            field=models.ManyToManyField(to='core.template'),
        ),
    ]
