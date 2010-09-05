"""
A way of retrieving unique, increasing values for use elsewhere in the system.

Based upon

    http://code.flickr.com/blog/2010/02/08/ticket-servers-distributed-unique- primary-keys-on-the-cheap/

but using insert + delete so that it works for databases without MySQL's
REPLACE functionality (thus, this version is somewhat less efficient than
Flick's, but out write load is significantly less as well).
"""

from django.db import models


class Manager(models.Manager):
    def new(self):
        obj = self.create()
        self.filter(counter__lt=obj.counter).delete()
        return obj.counter

class Ticket(models.Model):
    """
    A persistent counter. There will only ever be one of these in the database
    at a time.
    """
    counter = models.AutoField(primary_key=True)

    objects = Manager()

