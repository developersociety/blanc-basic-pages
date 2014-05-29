============
Installation
============

Requirements
============

Before installing blanc-basic-pages, you'll need a copy of Django__ 1.7,
django-mptt__ 0.6.1 and django-mptt-admin installed.

.. __: http://www.djangoproject.com/
.. __: https://github.com/django-mptt/django-mptt
.. __: https://github.com/leukeleu/django-mptt-admin


Installing blanc-basic-pages
============================

The fastest way of installing is to use pip__.

.. __: http://www.pip-installer.org/

Simply type::

    pip install blanc-basic-pages

Manual installation
-------------------

Alternative you manually install by downloading the latest version from the
`blanc-basic-pages page on the Python Package Index`__.

.. __: http://pypi.python.org/pypi/blanc-basic-pages/

Download the package, unpack it and run the ``setup.py`` installation
script::

    python setup.py install


Configuring your project
========================

Edit your Django project's settings module, ensure that the required
dependencies are installed and configured, then add ``blanc_basic_pages`` to
``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'mptt',
        'django_mptt_admin',
        ...
        'blanc_basic_pages',
    )

Once this is done, run ``python manage.py migrate`` to update your database.
