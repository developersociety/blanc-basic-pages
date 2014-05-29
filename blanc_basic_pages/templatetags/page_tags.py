from django import template
from django.core.urlresolvers import reverse
from django.utils import six
from blanc_basic_pages import get_page_model

register = template.Library()


@register.assignment_tag
def get_root_pages(current_page=None):
    # If given a string, this could either be:
    # - A Django URL (which can be reversed)
    # - A page URL
    if isinstance(current_page, six.string_types):
        try:
            current_page = get_page_model().objects.get(url=reverse(current_page))
        except get_page_model().DoesNotExist:
            current_page = None

    page_list = []

    # Find the root page so the template can highlight it
    if current_page:
        root_page = current_page.get_root()
    else:
        root_page = None

    for i in get_page_model().objects.root_nodes().filter(show_in_navigation=True):
        page_list.append((i, i == root_page))

    return page_list


@register.assignment_tag
def get_pages_at_level(current_page, level=1):
    page_and_ancestors = list(current_page.get_ancestors(include_self=True))

    # Page isn't deep enough to show this level of navigation
    if level > current_page.level + 1:
        return []

    parent_page = page_and_ancestors[level - 1]
    page_list = []

    for i in parent_page.get_children().filter(show_in_navigation=True):
        page_list.append((i, i in page_and_ancestors))

    return page_list
