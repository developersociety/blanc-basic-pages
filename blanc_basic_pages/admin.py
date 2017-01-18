from django.conf import settings
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .forms import PageAdminForm
from .models import Page


SHOW_LOGIN_REQUIRED = getattr(settings, 'PAGE_SHOW_LOGIN', False)


@admin.register(Page)
class PageAdmin(DjangoMpttAdmin):
    search_fields = ('url', 'title')
    form = PageAdminForm

    def get_fieldsets(self, request, obj=None):
        content = ['hero_image', 'content']
        advanced_options = ['template_name', 'published', 'login_required']

        if not getattr(settings, 'PAGE_SHOW_HERO_IMAGE', True):
            content.remove('hero_image')

        if not SHOW_LOGIN_REQUIRED:
            advanced_options.remove('login_required')

        fieldsets = (
            (None, {
                'fields': ('url', 'title'),
            }),
            ('Navigation', {
                'fields': ('parent', 'show_in_navigation'),
            }),
            ('Content', {
                'fields': content,
            }),
            ('Advanced options', {
                'fields': advanced_options,
            }),
        )
        return fieldsets

    def get_list_display(self, request):
        list_display = ['url', 'title', 'login_required']

        if not SHOW_LOGIN_REQUIRED:
            list_display.remove('login_required')

        return list_display

    def get_list_filter(self, request):
        list_filter = ['published', 'login_required']

        if not SHOW_LOGIN_REQUIRED:
            list_filter.remove('login_required')

        return list_filter
