# Generated by Django 4.2.1 on 2023-05-09 16:28

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='descript',
            field=models.TextField(max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Children', to='blog.subject', verbose_name='Родительская категория'),
        ),
    ]
