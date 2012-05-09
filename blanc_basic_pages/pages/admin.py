from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatpageForm
from django import forms
from django.conf import settings
from .models import Page


class PageAdminForm(forms.ModelForm):
    TEMPLATE_CHOICES = getattr(settings, 'PAGE_TEMPLATES', (
        ('', 'Default'),
    ))

    unique_url = forms.RegexField(
            label='URL', max_length=100, regex=r'^[-\w/\.~]+$',
            help_text="Example: '/about/contact/'. Make sure to have leading"
            " and trailing slashes.",
            error_message="This value must contain only letters, numbers,"
            " dots, underscores, dashes, slashes or tildes.")
    template_name = forms.ChoiceField(
            label='Template', choices=TEMPLATE_CHOICES, required=False)
    url = None

    class Meta(FlatpageForm.Meta):
        model = Page


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    actions = None
    fieldsets = (
        (None, {
            'fields': ('unique_url', 'title')
        }),
        ('Navigation', {
            'fields': ('parent', 'show_nav')
        }),
        ('Content', {
            'fields': ('content', 'sidebar')
        }),
        ('Advanced options', {
            'fields': ('template_name',)
        }),
    )
    list_display = ('url',)
    list_filter = ('enable_comments', 'registration_required')
    search_fields = ('url', 'title')


admin.site.unregister(FlatPage)
admin.site.register(Page, PageAdmin)
