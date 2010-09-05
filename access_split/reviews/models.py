import datetime

from django.core import validators
from django.db import models

class Review(models.Model):
    # The contrib.auth and products apps are in another db; no relations here.
    author_id = models.IntegerField()
    product_id = models.IntegerField()
    rating = models.PositiveIntegerField(null=True, validators=[
            validators.MaxValueValidator(5), validators.MinValueValidator(1)])
    text = models.TextField()
    created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return u"User %s reviews product %d (%s)" % (self.author_id,
                self.product_id, self.created.strftime("%H:%M, %b %d, %Y"))

    def delete(self, using=None):
        """
        Override default delete() to remove model from shadow as well as master
        db.
        """
        super(Review, self).delete(using)
        if using is None:
            super(Review, self).delete(using="reviews-s")
    delete.alters_data = True

    def in_shadow_db(self):
        """
        Returns True if this review also exists in the shadow database.
        """
        return self.__class__.objects.filter(id=self.id).exists()
    in_shadow_db.boolean = True

