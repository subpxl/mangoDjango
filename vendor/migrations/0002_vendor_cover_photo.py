# Generated by Django 4.1.4 on 2022-12-27 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='cover_photo',
            field=models.ImageField(blank=True, default='/images/default-profile.PNG', null=True, upload_to='users/profile_pictures'),
        ),
    ]