from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils.text import slugify
from django.utils import timezone
from sales.utils import generate_id
# Create your models here.


class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=255, null=True, blank=True)

    def get_product_name(self):
        return self.product.name

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product.name)
        self.price = self.product.price * self.quantity
        return super(Position, self).save(*args, **kwargs)


class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sales_man = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.transaction_id == '':
            self.transaction_id = generate_id()
        if self.created is None:
            self.created = timezone.now()

        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

    def __str__(self):
        return self.transaction_id


class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)
