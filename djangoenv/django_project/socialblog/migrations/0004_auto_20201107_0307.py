# Generated by Django 3.1.3 on 2020-11-07 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialblog', '0003_auto_20201107_0307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='c_image',
        ),
    ]
