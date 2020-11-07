# Generated by Django 3.1.3 on 2020-11-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialblog', '0002_post_campaign_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='campaign_image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
