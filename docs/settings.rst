========
Settings
========


PAGE_TEMPLATES
==============

Default::

    PAGE_TEMPLATES = (
        ('', 'Default'),
    )

A list of two-tuples in the format (``filename``, ``template name``). The
empty default template will use ``pages/default.html``.

You can add more template choices by extending this list::

    PAGE_TEMPLATES = (
        ('', 'Default'),
        ('pages/homepage.html', 'Home Page'),
    )

PAGE_SHOW_LOGIN
===============

Default: ``False``

Shows or hides the login required option in the pages Django admin. By default
this is ``False`` as most sites won't have a pages protected by username and
password authentication - so we hide it.

If your site needs certain pages to be protected so that only logged-in users
are able to view them, change this to ``True`` and then the option will appear
in the Django admin.

PAGE_SHOW_HERO_IMAGE
====================

Default: ``True``

Shows or hides the *Hero Image* field for pages in the Django admin. By default
this is ``True``, however if the site has no need for hero images in pages then
this can be turned off.
