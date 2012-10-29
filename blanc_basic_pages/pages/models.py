from django.db import models
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager
from blanc_basic_pages.pages import DEFAULT_MODEL


class BasePage(MPTTModel, FlatPage):
    unique_url = models.CharField('URL', max_length=100, unique=True)
    parent = TreeForeignKey(
            'self', null=True, blank=True, related_name='children')
    show_nav = models.BooleanField(
            'Show in navigation', default=True, db_index=True)

    objects = TreeManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.url = self.unique_url
        super(BasePage, self).save(*args, **kwargs)


# Only enable Page model if we aren't using a custom page model
if getattr(settings, 'BASIC_PAGE_MODEL', DEFAULT_MODEL) == DEFAULT_MODEL:
    class Page(BasePage):
        pass
