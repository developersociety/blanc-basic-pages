from django.utils.functional import SimpleLazyObject
from django.contrib.flatpages.models import FlatPage
from django.conf import settings
from django.utils.safestring import mark_safe


def flatpage(request):
    def get_flatpage():
        url = request.path_info

        # This has no chance of working
        if not url.endswith('/') and settings.APPEND_SLASH:
            return ''

        if not url.startswith('/'):
            url = '/' + url

        try:
            f = FlatPage.objects.get(url=url)
            f.title = mark_safe(f.title)
            f.content = mark_safe(f.content)
            return f
        except FlatPage.DoesNotExist:
            return ''

    return {
        'lazy_flatpage': SimpleLazyObject(get_flatpage),
    }
