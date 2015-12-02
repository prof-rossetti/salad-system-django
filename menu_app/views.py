from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    template = loader.get_template('menu_items/index.html')
    context = RequestContext(request, {
        'menu_item_list': [1,2,3,4],
    })
    return HttpResponse(template.render(context))
