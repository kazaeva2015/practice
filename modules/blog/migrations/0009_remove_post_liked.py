# Generated by Django 4.2.1 on 2023-05-10 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_subject_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
    ]
