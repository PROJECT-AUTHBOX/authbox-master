# Generated by Django 4.2 on 2023-10-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_globalsetting_ref_template_block_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsetting',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='globalsetting',
            name='order_item',
            field=models.PositiveIntegerField(default=0),
        ),
    ]