# Generated by Django 4.2.1 on 2023-05-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='Альт.название'),
        ),
    ]
