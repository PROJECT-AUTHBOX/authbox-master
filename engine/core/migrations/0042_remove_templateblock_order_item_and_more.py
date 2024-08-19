# Generated by Django 4.2 on 2023-10-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_remove_globalsetting_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templateblock',
            name='order_item',
        ),
        migrations.AddField(
            model_name='globalsetting',
            name='order_item',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
