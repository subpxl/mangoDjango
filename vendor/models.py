from django.db import models
from accounts.models import User, UserProfile

from accounts.utils import send_notification_email
# Create your models here.


class Vendor(models.Model):
    user = models.OneToOneField(
        User, related_name='user', on_delete=models.CASCADE)
    user_profile = models.OneToOneField(
        UserProfile, related_name='userprofile', on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=50)
    cover_photo = models.ImageField(
        upload_to='vendor/cover_photo', blank=True, null=True, default='/images/default-profile.PNG')
    banner = models.ImageField(
        upload_to='vendor/banner', blank=True, null=True, default='/images/default-profile.PNG')

    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    vendor_slug = models.SlugField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=255, null=True)
    vendor_license = models.ImageField(upload_to='vendor/license')
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    num_of_reviews = models.PositiveIntegerField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.vendor_name}'

    # def save(self, *args, **kwargs):
    #     if self.pk is not None:
    #         # upate
    #         orig = Vendor.objects.get(pk=self.pk)
    #         mail_template = 'accounts/emails/account_verification_email.html'
    #         context = {
    #             'user': self.user,
    #             'is_approved': self.is_approved,
    #         }
    #         if orig.is_approved != self.is_approved:
    #             if self.is_approved == True:
    #                 # send notification email
    #                 mail_subject = 'congratulations your account has been approved'
    #                 send_notification_email(
    #                     mail_subject, mail_template, context)
    #             else:
    #                 # send notification email
    #                 mail_subject = 'sorry your account is not eligible for selling on platform'
    #                 send_notification_email(
    #                     mail_subject, mail_template, context)

    #     return super(Vendor, self).save(*args, **kwargs)


class Links(models.Model):
    vendor = models.OneToOneField(
        Vendor,  on_delete=models.CASCADE)
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    tiktok = models.CharField(max_length=100, null=True)
    whatsapp = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)
    pinterest = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.vendor}'
