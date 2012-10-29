from django import template
from blanc_basic_pages.pages import get_page_model

register = template.Library()


@register.assignment_tag
def get_root_pages(current_page=None):
    page_list = []

    # Find the root page so the template can highlight it
    if current_page:
        root_page = current_page.get_root()
    else:
        root_page = None

    for i in get_page_model().objects.root_nodes().filter(show_nav=True):
        page_list.append((i, i == root_page))

    return page_list


@register.assignment_tag
def get_pages_at_level(page_level, current_page):
    page_and_ancestors = list(current_page.get_ancestors())
    page_and_ancestors.append(current_page)

    # Page isn't deep enough to show this level of navigation
    if page_level > current_page.level + 1:
        return []

    parent_page = page_and_ancestors[page_level - 1]
    page_list = []

    for i in parent_page.get_children().filter(show_nav=True):
        page_list.append((i, i in page_and_ancestors))

    return page_list
