from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('sandwichworks.views',
   (r'^$', 'show_index_page'),
   (r'menu/(?P<menu_slug>[-\w]+)/$', 'show_menu_page', { 'template_name':'menu/menu_body.html'},  'menu_view'),
   (r'pages/(?P<plain_slug>[-\w]+)/$', 'show_plain_page', { 'template_name':'sandwichworks/plain_page.html'},  'plain_view'),
)