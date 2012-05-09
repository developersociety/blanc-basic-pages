from django.db.models.signals import post_save
from django.contrib.sites.models import Site
from .models import Page


def flatpage_sites(sender, instance, **kwargs):
    instance.sites = [Site.objects.get_current()]

post_save.connect(flatpage_sites, sender=Page)
