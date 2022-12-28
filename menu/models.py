from django.db import models
from vendor.models import Vendor

# Create your models here.


class Category(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50, unique=True)
    category_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.category_name}'

    def clean(self):
        self.category_name = self.category_name.capitalize()


class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    num_of_reviews = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product')
    is_available = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_title}'


class Strain(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=300, null=True)
    type = models.CharField(max_length=300, null=True)
    dominant_terpene = models.CharField(max_length=300, null=True)
    top_reported_effect = models.CharField(max_length=300, null=True)
    thc = models.PositiveIntegerField(null=True)
    cbd = models.PositiveIntegerField(null=True)

    image = models.ImageField(upload_to='strain')

    def __str__(self):
        return f'{self.name }'


class Unit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
