============
Installation
============

Requirements
============

Before installing blanc-basic-pages, you'll need a copy of Django__ 1.4,
django-mptt__ 0.5 and django-mptt-treechangelist__ 0.1 installed.

.. __: http://www.djangoproject.com/
.. __: https://github.com/django-mptt/django-mptt
.. __: https://github.com/blancltd/django-mptt-treechangelist

The Django flatpages app is also required to be installed.


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

Edit your Django project's settings module, ensure that
``django.contrib.sites`` is already added to ``INSTALLED_APPS``, and add
``blanc_basic_pages.pages`` as well as the other required apps::

    INSTALLED_APPS = (
        'django.contrib.flatpages',
        ...
        'blanc_basic_pages.pages',
        'mptt',
        'mptt_treechangelist',
    )

Once this is done, run ``python manage.py syncdb`` to update your database.
