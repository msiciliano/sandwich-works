from django.db import models
from django.conf import settings

class SitePage(models.Model):
    page_title = models.CharField(max_length=50, unique=True, help_text='Unique title for this page. This will be used to create the URL and navigation. NOTE: Don\'t change this for the home page unless you really need something different than \"Home\"')
    site_name = settings.WEBSITE_NAME
    meta_keywords = models.CharField("Meta Keywords", max_length=255, help_text='Comma-deliniated set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for description meta tag')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
    def __unicode__(self):
        return self.page_title, "-", self.site_name
    
    @models.permalink
    def get_absolute_url(self):
        return ('basicwebsite_sitepage', (), {'sitepage_slug': self.slug})
    
class HeroAndFooterPage(SitePage):
    order_of_apperance = models.IntegerField(help_text='The order this day should appear in the NAVIGATION list', null=False)
    quote_image = models.ImageField(upload_to='header_footer')
    hero_quote =  models.CharField(max_length=255, blank=True, help_text='The text to be displayed under the branding image')
    main_site_image = models.ImageField(upload_to='header_footer')
    web_design_info = settings.WEB_DESIGN_INFO
    
    class Meta:
        ordering = ['order_of_apperance']
        
class ImageItem(models.Model):
    image_width = models.CharField(max_length=4, null=False)
    image_height = models.CharField(max_length=4, null=False)
    image_title = models.CharField(max_length=140, null=False)
    image_alt = models.CharField(max_length=140) 
    
    def __unicode__(self):
        return self.image_title       