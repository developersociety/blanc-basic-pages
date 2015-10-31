from django.conf import settings
from django.utils.functional import SimpleLazyObject

from .models import Page


def page(request):
    def get_page():
        url = request.path_info

        # This has no chance of working
        if not url.endswith('/') and settings.APPEND_SLASH:
            return ''

        if not url.startswith('/'):
            url = '/' + url

        try:
            return Page.objects.get(url=url)
        except Page.DoesNotExist:
            return ''

    return {
        'lazy_page': SimpleLazyObject(get_page),
    }
