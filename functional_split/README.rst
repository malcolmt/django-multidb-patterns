=================================================
1. Splitting data storage along functional lines
=================================================

In this example, the two main application models are in different databases.
All products are in the main (*default*) database, whilst product reviews are
in the "reviews" database.

Setup
======

To create the example databases, you need to run the ``syncdb`` command twice::

    python manage.py syncdb --noinput
    python manage.py syncdb --database reviews

An admin user will be created from an initial data fixture. Both the username
and password for this user are "*admin*" (without the quotes).

Trying out the code
====================

Start the development webserver::

    python manage.py runserver

Then point your web browser at http://localhost:8000/ and you will be able to
enter and view product reviews. The admin interface
(http://localhost:8000/admin/) can also be used to examine what is going on
behind the scenes.

