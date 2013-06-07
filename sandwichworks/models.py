from django.db import models
from django.core.urlresolvers import reverse
import basicwebsite
from basicwebsite.models import HeroAndFooterPage, ImageItem
import menus
from menus.models import Menu
# -*- coding: latin-1 -*-
    
class CarouselItem(ImageItem):
    image = models.ImageField(upload_to='carousel', null=False)
    display_name = models.CharField(max_length=255, help_text='The text to be displayed under the image for this carosel Item', null=False)
    order_of_apperance = models.IntegerField(help_text='The order this day should appear in the list', null=False, default=1)
    
    class Meta:
        ordering = ['order_of_apperance'] 
    
    def __unicode__(self):
        if not self.display_name:
            return u'Unknown Item'
        else:
            return u'%s' % self.display_name   
    
class HourOfOperation(models.Model):
    day_of_week = models.CharField(max_length=10, help_text='The the day of the week', null=False)
    order_of_apperance = models.IntegerField(help_text='The order this day should appear in the list', null=False)
    hours_open = models.CharField(max_length=20, help_text='The hours the store is open for this day', null=False)
    
    class Meta:
        ordering = ['order_of_apperance']  
        
    def __unicode__(self):
        if not self.day_of_week:
            return u'Unknown day'
        else:
            return u'%s' % self.day_of_week
    
class IndexPage(HeroAndFooterPage):
    street_address = models.CharField(max_length=100, blank=True, help_text='Number, Street, and suite only')
    city_and_state = models.CharField(max_length=150, blank=True, help_text='City, State and Zip Code')
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    order_of_appearance = -1
    carousel_caption = models.CharField(max_length=255, blank=True, help_text='The text to be displayed over the Carousel')
    hours_description = models.CharField(max_length=255, blank=True, help_text='The caption to display with the hours of operation. Like: Memorial Day Hours')   
    index_message = models.CharField(max_length=255, blank=True, help_text='This is any additional text you want to be seen under the email button')
    carousel_items = models.ManyToManyField(CarouselItem)
    hours_of_operation = models.ManyToManyField(HourOfOperation)
    is_active = True
    
    def get_absolute_url(self):
        return '/' 
    
    
class MenuPage(HeroAndFooterPage):
    menu_page_message_title = models.CharField(max_length=100, blank=True, help_text='OPTIONAL: The TITLE to be displayed OVER the message displayed at the bottom of the list of sidebars (if any)')
    menu_page_message = models.CharField(max_length=255, blank=True, help_text='OPTIONAL: The message TEXT to be displayed as a message at the bottom of the list of sidebars (if any)')
    menus_on_page = models.ManyToManyField(Menu, help_text='The specific menus with to be listed in this page')
    sidebars = models.ManyToManyField(Menu, blank=True, null=True, help_text='OPTIONAL: The specific sidebar menus with items to be listed in this page. These will not show pictures.', related_name="%(app_label)s_%(class)s_related")

    def get_absolute_url(self):
        return reverse('menu_view', kwargs={'menu_slug': self.slug})  
    