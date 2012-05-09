from django.db import models
from django.contrib.flatpages.models import FlatPage
from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager


class Page(MPTTModel, FlatPage):
    unique_url = models.CharField('URL', max_length=100, unique=True)
    parent = TreeForeignKey(
            'self', null=True, blank=True, related_name='children')
    show_nav = models.BooleanField(
            'Show in navigation', default=True, db_index=True)
    sidebar = models.TextField(blank=True)

    objects = TreeManager()

    def save(self, *args, **kwargs):
        self.url = self.unique_url
        super(Page, self).save(*args, **kwargs)
