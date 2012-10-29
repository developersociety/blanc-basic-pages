# The app/model used if no custom page is being used
DEFAULT_MODEL = 'pages.Page'


def get_page_model():
    from django.conf import settings
    from django.db.models import get_model

    page_model = getattr(settings, 'BASIC_PAGE_MODEL', DEFAULT_MODEL)
    app_label, model_name = page_model.split('.')
    return get_model(app_label, model_name)


# Avoid circular import
import listeners
