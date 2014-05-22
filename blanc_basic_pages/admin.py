from django.contrib import admin
from django.conf import settings
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Page


SHOW_LOGIN_REQUIRED = getattr(settings, 'PAGE_SHOW_LOGIN', False)


@admin.register(Page)
class PageAdmin(DjangoMpttAdmin):
    fieldsets = (
        (None, {
            'fields': ('url', 'title')
        }),
        ('Navigation', {
            'fields': ('parent', 'show_in_navigation')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Advanced options', {
            'fields': ('template_name', 'published') +
                      (('login_required',) if SHOW_LOGIN_REQUIRED else ()),
        }),
    )
    list_display = ('url', 'title')
    list_filter = ('published',) + (('login_required',) if SHOW_LOGIN_REQUIRED else ())
    search_fields = ('url', 'title')
