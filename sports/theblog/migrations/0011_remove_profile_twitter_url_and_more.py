# Generated by Django 4.1.7 on 2023-05-11 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_profile_fb_url_profile_instagram_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='twitter_url',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='website_url',
        ),
    ]
