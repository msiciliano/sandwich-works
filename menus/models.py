from django.db import models
import basicwebsite
from basicwebsite.models import ImageItem
# -*- coding: latin-1 -*-

class MenuItem(ImageItem):
    name = models.CharField(max_length=50, blank=True, help_text="The name of this menu item. Like: Turkey Sandwich")
    description = models.CharField(max_length=255, blank=True, help_text="A brief description that will appear under the name. Like: Our lean oven roasted Turkey, on your choice of bread ..." )
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    image = image = models.ImageField(upload_to='food_items', blank=True, null=True)
    order_number = models.IntegerField()
    
    def __unicode__(self):
        if not self.name:
            return  u'Unknown Item'
        else:
            return u'%s%s%s' % (self.name, " $", self.price)
    
    class Meta:
        ordering = ['order_number', 'name', 'price'] 

class Menu(models.Model):
    title = models.CharField(max_length=50, help_text="The name of this menu. Like: Roll Ups")
    description = models.CharField(max_length=255, blank=True, help_text="A brief description that will appear under the name Like: Our Roll-Ups are served on a large Pita or low-carb Pita and ... " )
    menu_items = models.ManyToManyField(MenuItem, help_text='The menu items that will be shown with this menu')
    order_number = models.IntegerField()
    
    def __unicode__(self):
        if not self.title:
            return u'Unknown Menu'
        else:
            return u'%s' % self.title
    
    class Meta:
        ordering = ['order_number', 'title']   
