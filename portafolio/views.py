from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, redirect
from models import Proyect



def index(request):
    p = Proyect.objects.all()[0]
    return direct_to_template(request, "portafolio/index.html", 
                              extra_context = { 'proyect':p })
def proyect(request, slug):
    p = get_object_or_404(Proyect, slug = slug)
    return direct_to_template(request, "portafolio/index.html", 
                              extra_context = { 'proyect':p })

def show_small(request):
    slug = request.GET.get("slug",None)
    p = get_object_or_404(Proyect, slug = slug)
    return direct_to_template(request, "portafolio/small.html", 
                              extra_context = { 'proyect':p })

def redirect(request):
    slug = request.GET.get("slug",None)
    if not None:
        return HttpResponseRedirect(reverse("portafolio-proyect", args= [slug]))
    else:
       raise Http404
