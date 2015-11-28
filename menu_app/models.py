from django.db import models

# Create your models here.

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55, unique=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "locations"

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location)
    title = models.CharField(max_length=200, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def location_id():
        return location

    class Meta:
        db_table = "menus"

class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    calories = models.PositiveIntegerField()
    gluten_free = models.BooleanField()
    vegan_safe = models.BooleanField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "menu_items"

class MenuItemRole(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu)
    menu_item = models.ForeignKey(MenuItem)
    category = models.CharField(max_length=255)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)

    def menu_id():
        return menu

    def menu_item_id():
        return menu_item

    class Meta:
        db_table = "menu_item_roles"
        unique_together = ("menu","menu_item")
        index_together = [["menu", "menu_item"]]
