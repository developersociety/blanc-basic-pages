from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


default_app_config = 'blanc_basic_pages.apps.BlancBasicPagesConfig'


def get_page_model():
    try:
        conf_model = getattr(settings, 'PAGE_MODEL', 'pages.Page')
        return django_apps.get_model(conf_model)
    except ValueError:
        raise ImproperlyConfigured("PAGE_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured("PAGE_MODEL refers to model '%s' that has not been installed" % conf_model)
