from django.db import models
from django.conf import settings
# -*- coding: latin-1 -*-

class SitePage(models.Model):
    page_title = models.CharField(max_length=50, unique=True, help_text='Unique title for this page. This will be used to create the URL and navigation')
    site_name = settings.WEBSITE_NAME
    meta_keywords = models.CharField("Meta Keywords", max_length=255, help_text='Comma-deliniated set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255, help_text='Description of this page\'s content (for meta tag)')
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for page URL (created from the page_title).  You should not change this field directly without good reason')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
    def __unicode__(self):
        if not self.page_title:
            return u'Unknown Page'
        else:
            return u'%s%s%s' % (self.page_title, "-", self.site_name)
    
class HeroAndFooterPage(SitePage):
    order_of_appearance = models.IntegerField(help_text='The order this day should appear in the NAVIGATION list', null=False)
    quote_image = models.ImageField(upload_to='header_footer', help_text='This pic should be between 400-450 pixels wide and 100-175 pixel high')
    hero_quote =  models.CharField(max_length=255, blank=True, help_text='The \"quote\" or text to be displayed under the quote image')
    main_page_image = models.ImageField(upload_to='header_footer',  help_text='This pic should be between 400-450 pixels wide and 250-300 pixel high')
    web_design_info = settings.WEB_DESIGN_INFO
    
    class Meta:
        ordering = ['order_of_appearance']
        
        
class ImageItem(models.Model):
    image_title = models.CharField(max_length=140, blank=True, help_text="This is what will be used to describe the image. It will also show up as a tool tip if you hover your mouse over the image")
    image_alt = models.CharField(max_length=140, blank=True, help_text="This is for people without the actual image. Like if they are blind and reading from a reader, \n or the image could not be displayed. It will describe the image to them") 
    
    def __unicode__(self):
        if not self.image_title:
            return u'Unknown Image'
        else:
            return u'%s' % self.image_title      