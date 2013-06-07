from django.shortcuts import get_object_or_404, render_to_response
from django.conf import settings
from django.template import RequestContext
from django.db.models.fields.related import ReverseManyRelatedObjectsDescriptor
from django.db.models.query import QuerySet
from menus.models import Menu, MenuItem
from sandwichworks.models import IndexPage, MenuPage, CarouselItem, HourOfOperation

def show_index_page(request, template_name="sandwichworks/index.html"):
    index_page = get_object_or_404(IndexPage, page_title=settings.INDEX_TITLE)
    page = get_herounit_vars(index_page)
    carousel_caption = index_page.carousel_caption
    hours_description = index_page.hours_description
    hours = index_page.hours_of_operation.all()
    index_message = index_page.index_message
    carousel_items = index_page.carousel_items.all()
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def show_menu_page(request, menu_slug, template_name="menu/menu_body.html"):
    menu_page = get_object_or_404(MenuPage, slug=menu_slug)
    page = get_herounit_vars(menu_page)
    menus_on_page =  add_menus(menu_page.menus_on_page.all()) 
    sidebars =  add_menus(menu_page.sidebars.all())
    
    """ This effectively sets a limit on the height and width the menu """
    menu_size = []
    for i in range(settings.MENU_ITEM_LIMIT):
        if i > 1 and i % settings.MENU_WIDTH == 0:
            menu_size.append(i)
    
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
        
def get_herounit_vars(page):
    page_title = page.page_title
    quote_image = page.quote_image
    hero_quote = page.hero_quote
    main_site_image = page.main_page_image
    meta_keywords = page.meta_keywords
    meta_description = page.meta_description
    web_design_info = page.web_design_info
    return locals()

def add_menus(menu_list):
    if not isinstance(menu_list, QuerySet):
        raise RuntimeError("Unable to add menus from Object %s" % type(menu_list))
    
    menus = []
    for menu_instance in menu_list:
        
        if isinstance(menu_instance, Menu):
            menu_items = []
            for menu_item in menu_instance.menu_items.all():
                menu_items.append(menu_item)
                                  
            menus.append({'menu_instance':menu_instance, 'menu_items':menu_items})
        else: 
            raise RuntimeError("Method only supports Menu lists")
        
    return menus    
        