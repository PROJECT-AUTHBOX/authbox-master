# Generated by Django 4.2.4 on 2023-08-31 17:47

from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0033_pagestranslation_sub_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='share_count',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='share count'),
        ),
        migrations.AddField(
            model_name='document',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(blank=True, to='frontend.tags', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='document',
            name='view_count',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='view count'),
        ),
        migrations.AddField(
            model_name='pages',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.categories'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.categories'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='tags',
            field=models.ManyToManyField(blank=True, to='frontend.tags', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.categories'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='frontend.tags', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='document',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.categories'),
        ),
        migrations.AlterField(
            model_name='events',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.categories'),
        ),
        migrations.AlterField(
            model_name='events',
            name='tags',
            field=models.ManyToManyField(blank=True, to='frontend.tags', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='news',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.categories'),
        ),
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, to='frontend.tags', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='tags',
            field=models.ManyToManyField(blank=True, to='frontend.tags', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='pagestranslation',
            name='sub_title',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=500, null=True, verbose_name='sub title')),
        ),
    ]
