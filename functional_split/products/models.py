from django.db import models

class Product(models.Model):
    """
    An abstract product description.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Stock(models.Model):
    """
    Track the inventory of a single product.
    """
    product = models.OneToOneField(Product)
    quantity = models.PositiveIntegerField()  # (Django permits 0 here)

    class Meta:
        verbose_name_plural = "stock"

    def __unicode__(self):
        return u"%s, quantity %d" % (self.product, self.quantity)

