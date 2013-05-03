from django.db import models
import basicwebsite
from basicwebsite.models import HeroAndFooterPage, ImageItem
import menu
from menu.models import Menu
    
class CarouselItem(ImageItem):
    image = models.ImageField(upload_to='carousel', null=False)
    display_name = models.CharField(max_length=255, help_text='The text to be displayed under the image for this carosel Item', null=False)
    order_of_apperance = models.IntegerField(help_text='The order this day should appear in the list', null=False, default=1)
    
    class Meta:
        ordering = ['order_of_apperance'] 
    
    def __unicode__(self):
        return self.display_name   
    
class HourOfOperation(models.Model):
    day_of_week = models.CharField(max_length=10, help_text='The the day of the week', null=False)
    order_of_apperance = models.IntegerField(help_text='The order this day should appear in the list', null=False)
    hours_open = models.CharField(max_length=20, help_text='The hours the store is open for this day', null=False)
    
    class Meta:
        ordering = ['order_of_apperance']  
        
    def __unicode__(self):
        return self.day_of_week
    
class IndexPage(HeroAndFooterPage):
    street_address = models.CharField(max_length=100, blank=True, help_text='Number, Street, and suite only')
    city_and_state = models.CharField(max_length=150, blank=True, help_text='City, State and Zip Code')
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    order_of_appearance = -1
    carousel_caption = models.CharField(max_length=255, blank=True, help_text='The text to be displayed under the over the Carousel')
    hours_description = models.CharField(max_length=255, blank=True, help_text='The caption to display with the hours of operation. Like: Memorial Day Hours')   
    index_message = models.CharField(max_length=255, blank=True, help_text='This is any additional text you want to be seen under the email button')
    carousel_items = models.ManyToManyField(CarouselItem)
    hours_of_operation = models.ManyToManyField(HourOfOperation)
    is_active = True
    
    
class MenuPage(HeroAndFooterPage):
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for page URL created from the page_title')
    menu_page_name = models.CharField(max_length=100, help_text='')
    menus = models.ManyToManyField(Menu, help_text='The specific menus to be listed in this page')
