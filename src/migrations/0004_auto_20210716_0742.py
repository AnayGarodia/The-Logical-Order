# Generated by Django 3.1.3 on 2021-07-16 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='age',
        ),
        migrations.RemoveField(
            model_name='files',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='files',
            name='name',
        ),
    ]
