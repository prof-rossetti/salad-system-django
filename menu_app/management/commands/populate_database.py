import code # to debug: `code.interact(local=locals())` or `code.interact(local=dict(globals(), **locals()))`
from django.core.management.base import BaseCommand, CommandError
from menu_app.models import MenuItem

class Command(BaseCommand):
    help = 'Adds menu items to the database'

    def handle(self, *args, **options):

        # CREATE MENU ITEMS

        menu_items = [
            {
                #"category": 'SignatureSalad',
                "title": 'TEST SALAD',
                "calories": 1111,
                "gluten_free": 0,
                "vegan_safe": 1,
                "description": 'a salad to use when testing the web application.'
            },
            {
                #"category": 'SeasonalSalad',
                "title": 'KALE YEAH',
                "calories": 540,
                "gluten_free": 0,
                "vegan_safe": 1,
                "description": 'a kale-based salad.'
            },
            {
                #"category": 'SignatureGrain',
                "title": 'NEWTON',
                "calories": 720,
                "gluten_free": 1,
                "vegan_safe": 0,
                "description": 'a fall salad with apples.'
            }
        ]

        for mi in menu_items:
            menu_item = MenuItem(
                title = mi["title"],
                calories = mi["calories"],
                gluten_free = mi["gluten_free"],
                vegan_safe = mi["vegan_safe"],
                description = mi["description"]
            )
            try:
                menu_item.save()
            except Exception as e:
                print(e)

        # COUNT AND PRINT MENU ITEMS

        item_count = MenuItem.objects.count()
        self.stdout.write("THERE ARE %s ITEMS" % item_count)
