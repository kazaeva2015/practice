# Generated by Django 4.2.1 on 2023-05-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=255, verbose_name='Альт.название'),
        ),
    ]
