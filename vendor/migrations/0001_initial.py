# Generated by Django 4.1.4 on 2022-12-27 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('vendor_slug', models.SlugField(blank=True, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('vendor_license', models.ImageField(upload_to='vendor/license')),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=100, null=True)),
                ('instagram', models.CharField(max_length=100, null=True)),
                ('twitter', models.CharField(max_length=100, null=True)),
                ('linkedin', models.CharField(max_length=100, null=True)),
                ('tiktok', models.CharField(max_length=100, null=True)),
                ('whatsapp', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=100, null=True)),
                ('pinterest', models.CharField(max_length=100, null=True)),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]
