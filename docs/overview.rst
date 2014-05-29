========
Overview
========


What is blanc-basic-pages?
==========================

blanc-basic-pages is a simple Django package which acts as a replacement for
:py:mod:`~django.contrib.flatpages`.

Certain features of flatpages have been removed to make administration easier,
and other features have been added.


Design notes
============

Page Tree
---------

Pages uses the django-mptt__ package to organise the page tree hierarchy. By
using a page tree it allows site managers to use the Django admin to organise
the navigation used on the site without having to edit any templates.

.. __: https://github.com/django-mptt/django-mptt

Sites framework removed
-----------------------

To remove complexity, the :py:mod:`~django.contrib.sites` framework dependency
has been removed. This removes the risk of the same URL being used multiple
times and causing a ``MultipleObjectsReturned`` exception, as well as making
it easier to use a page tree.

Templates configurable as a setting
-----------------------------------

The admin for pages limits the options for templates to the choices available
in the select box. Site staff can pick a defined template instead of having to
enter the filename of a template.

This list of templates is configurable as ``PAGE_TEMPLATES`` in your project
settings file.

Errors will generate exceptions
-------------------------------

Flatpages catches any exceptions and serves an error 404 page, which is a sane
default given that site staff can cause problems by choosing an invalid
template. As the pages admin restricts this, any exceptions for pages will be
raised and not ignored.
