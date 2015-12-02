import code # to debug: `code.interact(local=locals())` or `code.interact(local=dict(globals(), **locals()))`
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Menu, MenuItem

# Create your views here.

def index(request):
    template = loader.get_template('menus/index.html')
    menus = Menu.objects.all()
    context = RequestContext(request, {'menus': menus})
    return HttpResponse(template.render(context))

def show(request, menu_id):
    print "fun times"
    print menu_id
    template = loader.get_template('menus/show.html')
    menu = Menu.objects.first() #todo: get based on request params, and move this method into menus/<id>
    #menu_item_roles = menu.menuitemrole_set.all()
    #menu_item_role = menu_item_roles.first()
    #menu_item = menu_item_role.menu_item
    #menu_items = MenuItem.objects.select_related().all()
    context = RequestContext(request, {
        'menu': menu#,
        #'items': menu_items
    })
    return HttpResponse(template.render(context))
