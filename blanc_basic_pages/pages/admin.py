from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatpageForm
from django import forms
from django.conf import settings
from blanc_basic_pages.pages import DEFAULT_MODEL, get_page_model
from mptt_treechangelist.admin import TreeModelAdmin


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
        model = get_page_model()


class PageAdmin(TreeModelAdmin):
    form = PageAdminForm
    fieldsets = (
        (None, {
            'fields': ('unique_url', 'title')
        }),
        ('Navigation', {
            'fields': ('parent', 'show_nav')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Advanced options', {
            'fields': ('template_name',)
        }),
    )
    list_display = ('url',)
    list_filter = ('enable_comments', 'registration_required')
    search_fields = ('url', 'title')


admin.site.unregister(FlatPage)

# Only enable Page admin if a custom model isn't being used
if getattr(settings, 'BASIC_PAGE_MODEL', DEFAULT_MODEL) == DEFAULT_MODEL:
    admin.site.register(get_page_model(), PageAdmin)
