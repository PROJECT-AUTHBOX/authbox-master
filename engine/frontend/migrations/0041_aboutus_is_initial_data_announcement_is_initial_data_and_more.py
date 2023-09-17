# Generated by Django 4.2 on 2023-09-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0040_product_price_product_price_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='announcement',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='banner',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='categories',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dailyalert',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='document',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='events',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fasilities',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='favicon',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='googlecalendar',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='googlecalendardetail',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='greeting',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='howitworks',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='location',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='logo',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offers',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pages',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='photogallery',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='popup',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchasing',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='relatedlink',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='slideshow',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tags',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testimony',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videogallery',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='whyus',
            name='is_initial_data',
            field=models.BooleanField(default=False),
        ),
    ]
