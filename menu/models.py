from django.db import models
import basicwebsite
from basicwebsite.models import ImageItem

class FoodItem(ImageItem):
    image = models.ImageField(upload_to='food')    
    

class MenuItem(models.Model):
    item_name = models.CharField(max_length=50, blank=True, help_text="The name of this menu item. Like: Turkey Sandwich")
    item_description = models.CharField(max_length=255, blank=True, help_text="A brief description that will appear under the name. Like: Our lean oven roasted Turkey, on your choice of bread ..." )
    item_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    item_image = models.ManyToManyField(FoodItem)
    order_number = models.IntegerField()
    
    def __unicode__(self):
        return self.item_name, " ", self.item_price
    
class Menu(models.Model):
    menu_name = models.CharField(max_length=50, help_text="The name of this menu. Like: Roll Ups")
    menu_description = models.CharField(max_length=255, blank=True, help_text="A brief description that will appear under the name Like: Our Roll-Ups are served on a large Pita or low-carb Pita and ... " )
    menu_items = models.ManyToManyField(MenuItem, help_text='The menu items that will be shown with this menu')
    order_number = models.IntegerField()
    ordering = ['order_number', 'item_name', 'item_price']
    
    def __unicode__(self):
        return self.menu_name
    
    

    
