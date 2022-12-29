# Generated by Django 4.1.4 on 2022-12-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_userprofile_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='/images/default-cover.PNG', null=True, upload_to='users/cover_photos'),
        ),
    ]