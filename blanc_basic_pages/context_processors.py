from django.utils.functional import SimpleLazyObject
from django.conf import settings
from . import get_page_model


def page(request):
    def get_page():
        url = request.path_info

        # This has no chance of working
        if not url.endswith('/') and settings.APPEND_SLASH:
            return ''

        if not url.startswith('/'):
            url = '/' + url

        try:
            return get_page_model().objects.get(url=url)
        except get_page_model().DoesNotExist:
            return ''

    return {
        'lazy_page': SimpleLazyObject(get_page),
    }
