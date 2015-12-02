from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import MenuItem

# Create your views here.

def index(request):
    template = loader.get_template('menu_items/index.html')
    menu_items = MenuItem.objects.all()
    context = RequestContext(request, {'menu_items': menu_items})
    return HttpResponse(template.render(context))
