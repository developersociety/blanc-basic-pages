from __future__ import unicode_literals

from blanc_basic_assets.fields import AssetForeignKey
from django.core.exceptions import ValidationError
from django.core.urlresolvers import get_script_prefix
from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import iri_to_uri, python_2_unicode_compatible

from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey


# Validator from flatpages
url_validator = RegexValidator(regex=r'^[-\w/\.~]+$',
                               message="This value must contain only letters, numbers, dots, "
                                       "underscores, dashes, slashes or tildes.")


# Another validator to ensure the URL starts and ends with a slash
def slash_validator(url):
    if not url.startswith('/'):
        raise ValidationError("This value must start with a leading slash.")
    elif not url.endswith('/'):
        raise ValidationError("This value must end with a trailing slash.")


@python_2_unicode_compatible
class Page(MPTTModel):
    url = models.CharField(
        'URL', max_length=100, unique=True,
        help_text="Example: '/about/contact/'. Make sure to have leading and trailing slashes.",
        validators=[url_validator, slash_validator])
    title = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    show_in_navigation = models.BooleanField(default=True, db_index=True)
    hero_image = AssetForeignKey('assets.Image', blank=True, null=True, on_delete=models.SET_NULL)
    content = models.TextField(blank=True)
    template_name = models.CharField(max_length=100, blank=True)
    published = models.BooleanField(default=True, db_index=True)
    login_required = models.BooleanField(default=False, db_index=True)

    objects = TreeManager()

    def __str__(self):
        return '%s -- %s' % (self.url, self.title)

    def get_absolute_url(self):
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)
