from django.contrib import admin
import menu
from menu.models import MenuItem, Menu
import sandwichworks
from sandwichworks.models import IndexPage, MenuPage, HourOfOperation, CarouselItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_description', 'item_price', 'order_number')
    list_display_links = ('item_name',)
    list_per_page = 50
    ordering = ['item_name']
    search_fields = ('item_name', 'item_description')
  
admin.site.register(MenuItem, MenuItemAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'menu_description', 'order_number')
    list_display_links = ('menu_name', )
    list_per_page = 5
    ordering = ['order_number']
    search_fields = ('menu_name', 'menu_description')
    #prepopulated_fields = {'slug': ('name',)}
      
admin.site.register(Menu, MenuAdmin)           

class IndexPageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'hero_quote', 'carousel_caption', 'hours_description', 'index_message', 'is_active')
    list_display_links = ('page_title', )
    list_per_page = 1
    
admin.site.register(IndexPage, IndexPageAdmin)

class MenuPageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'meta_keywords', 'meta_description', 'is_active', 'quote_image', 'hero_quote', 'main_site_image', 'menu_page_name', 'is_active',)
    list_display_links = ('page_title', )
    list_per_page = 5  
    ordering = ['page_title']
    prepopulated_fields = {'slug': ('page_title', )}

admin.site.register(MenuPage, MenuPageAdmin)

class HourOfOperationAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'hours_open', 'order_of_apperance')
    list_display_links = ('day_of_week', )
    list_per_page = 8
    ordering = ['order_of_apperance']
    
admin.site.register(HourOfOperation, HourOfOperationAdmin)    

class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('order_of_apperance', 'image', 'display_name', 'image_width', 'image_height')
    list_per_page = 8
    ordering = ['order_of_apperance']
    
admin.site.register(CarouselItem, CarouselItemAdmin)    