=====================================================
3. Sharding data storage for reviews
=====================================================

This is the third of three examples of multiple database use. In this example,
the initial setup is extended to add three databases for reviews
(*"reviews-1"*, *"reviews-2"*, *"reviews-3"*). Review records are stored in one
of these databases, based on a hash of their primary key value. In large-scale
production environments, this would distribute the read and write load evenly
across a large database cluster. It could also be further combined with
database replication and read-only slave databases for separate read and write
loads.

All product information is still in the main (*"default"*) database, as before.

Setup
======

To create the example databases, you need to run the ``syncdb`` command four
times::

    python manage.py syncdb --noinput
    python manage.py syncdb --database reviews-1
    python manage.py syncdb --database reviews-2
    python manage.py syncdb --database reviews-3

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

Reviews are immediately viewable to everybody after being created (in contrast
to the second simulated example). However, they are distributed more or less
evenly (in the long run) across the three databases. You can see this by using
the SQLite command line client to examine the `reviews_review` table in each of
the *reviews-X* databases.

At the present time, the admin interface only displays review results from the
*"reviews-1"* database.

Development exercise
---------------------

An exercise in admin customization would be to add a way (via a request
parameter to the changelist page) to control which database's results are shown
and then add a link on the changelist page for reviews to control viewing on a
per-database level.

