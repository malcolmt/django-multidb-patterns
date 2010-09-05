import datetime
import hashlib

from django.conf import settings
from django.core import validators
from django.db import models, router
from django.db.models import query

from ticketing.models import Ticket


# XXX: The QuerySet and Manager overrides here are because Django's default
# queryset methods will *never* end up calling db_for_write() with an instance
# as part of QuerySet.create() or QuerySet.get_or_create().

class QuerySet(query.QuerySet):
    @property
    def db(self):
        """
        When writing to sharded database, the concept of a sensible default
        based on the model alone doesn't make sense (i.e. we always need
        "instance" in db_for_write()). So we avoid that situation here.
        """
        if self._for_write:
            return self._db
        return self._db or router.db_for_read(self.model)

class Manager(models.Manager):
    def get_query_set(self):
        return QuerySet(self.model, using=self._db)

    @property
    def db(self):
        return None

class Review(models.Model):
    # The contrib.auth and products apps are in another db; no relations here.
    author_id = models.IntegerField()
    product_id = models.IntegerField()
    rating = models.PositiveIntegerField(null=True, validators=[
            validators.MaxValueValidator(5), validators.MinValueValidator(1)])
    text = models.TextField()
    created = models.DateTimeField(default=datetime.datetime.now)

    objects = Manager()

    # Explicit primary key, as this is used to find the database for saving.
    id = models.IntegerField(default=Ticket.objects.new, primary_key=True)

    def __unicode__(self):
        return u"User %s reviews product %d (%s)" % (self.author_id,
                self.product_id, self.created.strftime("%H:%M, %b %d, %Y"))

    def get_db_num(self):
        """
        Returns the database alias that stores the data for this instance.
        """
        return 1 + (int(hashlib.md5(str(self.id)).hexdigest(), 16) %
                settings.CLUSTER_SIZE)

