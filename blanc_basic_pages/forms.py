from django import forms
from django.conf import settings

from .models import Page


TEMPLATE_CHOICES = getattr(settings, 'PAGE_TEMPLATES', (
    ('', 'Default'),
))


class BasePageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ()


def page_admin_form():
    class PageAdminForm(BasePageAdminForm):
        template_name = forms.ChoiceField(choices=TEMPLATE_CHOICES, required=False)

    return PageAdminForm
