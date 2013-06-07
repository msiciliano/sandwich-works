from django.conf import settings
import sandwichworks
from sandwichworks.models import IndexPage, MenuPage

def sandwichworks(request):
    
    active_pages =  []
    for x in IndexPage.objects.filter(is_active=True):
        active_pages.append(x)
    
    for x in MenuPage.objects.filter(is_active=True):
        active_pages.append(x)
    
    return {
        'active_pages':active_pages,
        'site_name': settings.WEBSITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCRIPTION,
        'copyright_info': settings.COPYRIGHT_INFO,
        'website_design_info': settings.WEB_DESIGN_INFO,
        'street_address': settings.STREET_ADDRESS,
        'city_and_state': settings.CITY_AND_STATE,
        'phone_number': settings.PHONE_NUMBER,
        'email': settings.EMAIL,
        'request': request
    }
    
    
    