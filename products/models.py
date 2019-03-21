from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    regular_price = models.IntegerField()
    final_price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    category = models.ForeignKey(
        ProductCategory, related_name='products',
        blank=True, null=True, on_delete=models.SET_NULL)
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
