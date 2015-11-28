from django.contrib import admin
from .models import Location, Menu, MenuItem, MenuItemRole

# Register your models here.

admin.site.register(Location)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(MenuItemRole)
