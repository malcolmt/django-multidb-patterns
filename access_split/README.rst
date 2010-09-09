=====================================================
2. Splitting data storage along access pattern lines
=====================================================

This is the second of three examples of multiple database use. In this example,
the initial setup is extended to add a second database for reviews that is used
for read-only access. All writes go to the main (*"reviews"*) database, whilst
reads come from the shadow (*"reviews-s"*) database.

All product information is still in the main (*"default"*) database, as before.

Setup
======

To create the example databases, you need to run the ``syncdb`` command three
times::

    python manage.py syncdb --noinput
    python manage.py syncdb --database reviews
    python manage.py syncdb --database reviews-s

An admin user will be created from an initial data fixture. Both the username
and password for this user are *"admin"* (without the quotes).

Trying out the code
====================

Start the development webserver::

    python manage.py runserver

Then point your web browser at http://localhost:8000/ and you will be able to
enter and view product reviews. The admin interface
(http://localhost:8000/admin/) can also be used to examine what is going on
behind the scenes.

Any time a new review is created, it is initially only written to the main
reviews database and the review creator has all subsequent reads come from that
database for five minutes (in a production environment, this would allow time
for data to be synchronized to the slave installs). If you use a second web
browser to view the local site after creating a review, you will notice that
the second view (who is seeing the shadow reviews database) cannot see the new
review.

In the admin interface, you will see there are some extra admin actions for
copying a record from the main reviews database to the shadow and for deleting
reviews (which also removes them from the shadow database).

