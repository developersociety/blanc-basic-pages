from django.db.models.signals import post_save
from django.contrib.sites.models import Site
from blanc_basic_pages.pages import get_page_model


def flatpage_sites(sender, instance, raw, **kwargs):
    if not raw:
        instance.sites = [Site.objects.get_current()]

post_save.connect(flatpage_sites, sender=get_page_model())
