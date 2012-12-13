from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.sites.models import Site
from blanc_basic_pages.pages import DEFAULT_MODEL


def flatpage_sites(sender, instance, raw, **kwargs):
    if not raw:
        instance.sites = [Site.objects.get_current()]


if getattr(settings, 'BASIC_PAGE_MODEL', DEFAULT_MODEL) == DEFAULT_MODEL:
    from blanc_basic_pages.pages.models import Page
    post_save.connect(flatpage_sites, sender=Page)
