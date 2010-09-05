from django.db import models

class Product(models.Model):
    """
    An abstract product description.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

