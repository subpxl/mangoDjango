from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'
