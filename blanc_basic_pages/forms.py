from django import forms
from django.conf import settings

from .models import Page


TEMPLATE_CHOICES = getattr(settings, 'PAGE_TEMPLATES', (
    ('', 'Default'),
))


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)

        # The list of templates is defined in settings, however as we can't have dynamic choices in
        # models due to migrations - we change the form choices instead.
        self.fields['template_name'] = forms.ChoiceField(choices=TEMPLATE_CHOICES, required=False)
