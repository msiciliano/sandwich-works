from django.contrib import admin
import menus
from menus.models import MenuItem, Menu
import sandwichworks
from sandwichworks.models import IndexPage, MenuPage, HourOfOperation, CarouselItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'order_number')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['name']
    search_fields = ('name', 'description', 'price')
  
admin.site.register(MenuItem, MenuItemAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order_number')
    list_display_links = ('title', )
    list_per_page = 5
    ordering = ['order_number']
    search_fields = ('title', 'description')
      
admin.site.register(Menu, MenuAdmin)           

class IndexPageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'hero_quote', 'carousel_caption', 'hours_description', 'index_message', 'is_active')
    list_display_links = ('page_title', )
    list_per_page = 1
    prepopulated_fields = {'slug': ('page_title', )}
    
admin.site.register(IndexPage, IndexPageAdmin)

class MenuPageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'page_title', 'meta_keywords', 'meta_description', 'is_active', 'quote_image', 'hero_quote', 'main_page_image', 'is_active')
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
    list_display = ('order_of_apperance', 'image', 'display_name')
    list_per_page = 8
    ordering = ['order_of_apperance']
    
admin.site.register(CarouselItem, CarouselItemAdmin)    