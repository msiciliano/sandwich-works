from django.shortcuts import get_object_or_404, render_to_response
from django.conf import settings
from django.template import RequestContext
from sandwichworks.models import IndexPage, MenuPage, CarouselItem, HourOfOperation

def index(request, template_name="sandwichworks/index.html"):
    index_page = get_object_or_404(IndexPage, page_title=settings.INDEX_TITLE)
    page = get_herounit_vars(index_page)
    carousel_caption = index_page.carousel_caption
    hours_description = index_page.hours_description
    hours = index_page.hours_of_operation.all()
    index_message = index_page.index_message
    carousel_items = index_page.carousel_items.all()
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def menu_page(request, sitepage_slug, menu_body_template_name="menu_body.html", menu_template_name="menu.html", menu_item_template_name="menu_list_item.html"):
    menu_page = get_object_or_404(MenuPage, slug=sitepage_slug)
    get_herounit_vars(menu_page)
    menus = menu_page.menus_set.all()
        
def get_herounit_vars(request_page):
    page_title = request_page.page_title
    quote_image = request_page.quote_image
    hero_quote = request_page.hero_quote
    main_site_image = request_page.main_site_image
    meta_keywords = request_page.meta_keywords
    meta_description = request_page.meta_description
    web_design_info = request_page.web_design_info
    return locals()