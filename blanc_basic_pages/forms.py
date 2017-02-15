from django import forms
from django.conf import settings

from mptt.forms import MPTTAdminForm

from .models import Page


TEMPLATE_CHOICES = getattr(settings, 'PAGE_TEMPLATES', (
    ('', 'Default'),
))


class PageAdminForm(MPTTAdminForm):
    class Meta:
        model = Page
        exclude = ()
        widgets = {
            # The list of templates is defined in settings, however as we can't have dynamic
            # choices in models due to migrations - we change the form choices instead.
            'template_name': forms.widgets.Select(choices=TEMPLATE_CHOICES),
        }
