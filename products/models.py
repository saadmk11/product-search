from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64)


class Product(models.Model):
    name = models.CharField(max_length=128)
    regular_price = models.DecimalField(max_digits=8, decimal_places=2)
    final_price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    category = models.ManyToManyField(
        ProductCategory, related_name='products')
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def discount(self):
        if self.regular_price <= self.final_price:
            return None
        return (self.regular_price - self.final_price)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']
