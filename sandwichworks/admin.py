from django.contrib import admin
import menus
from menus.models import MenuItem, Menu
import sandwichworks
from sandwichworks.models import IndexPage, MenuPage, PlainPageContent, HourOfOperation, CarouselItem, PlainPage

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name',  'price', 'order_number', 'image', 'image_title', 'image_alt')
    list_display_links = ('name', 'price', 'order_number')
    list_per_page = 50
    ordering = ['name']
    search_fields = ('name', 'description', 'price')
  
admin.site.register(MenuItem, MenuItemAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_number')
    list_display_links = ('title', )
    list_per_page = 5
    ordering = ['order_number']
    search_fields = ('title', 'description')
      
admin.site.register(Menu, MenuAdmin)           

class IndexPageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'order_of_appearance', 'is_active', 'hero_quote', 'carousel_caption', 'hours_description', 'index_message')
    list_display_links = ('page_title', )
    list_per_page = 1
    prepopulated_fields = {'slug': ('page_title', )}
    
admin.site.register(IndexPage, IndexPageAdmin)

class MenuPageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'order_of_appearance', 'is_active', 'quote_image', 'hero_quote', 'main_page_image')
    list_display_links = ('page_title', )
    list_per_page = 5  
    ordering = ['page_title']
    prepopulated_fields = {'slug': ('page_title', )}

admin.site.register(MenuPage, MenuPageAdmin)

class HourOfOperationAdmin(admin.ModelAdmin):
    list_display = ('order_of_appearance', 'day_of_week', 'hours_open')
    list_display_links = ('day_of_week', )
    list_per_page = 8
    ordering = ['order_of_appearance']
    
admin.site.register(HourOfOperation, HourOfOperationAdmin)    

class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('order_of_appearance', 'display_name', 'image', )
    list_per_page = 8
    ordering = ['order_of_appearance']
    
admin.site.register(CarouselItem, CarouselItemAdmin)    

class PlainPageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'order_of_appearance', 'is_active',)
    list_per_page = 10
    ordering = ['order_of_appearance']
    prepopulated_fields = {'slug': ('page_title', )}
    
admin.site.register(PlainPage, PlainPageAdmin) 

class PlainPageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_of_appearance', 'image' )
    ordering = ['order_of_appearance']
    
admin.site.register(PlainPageContent, PlainPageContentAdmin)      