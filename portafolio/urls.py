from django.conf.urls.defaults import *

urlpatterns = patterns('portafolio.views',
    url(r"^$", "index", name="portafolio-index"),
    url(r"^small/$", "show_small", name="portafolio-small"),
    url(r"^redirect/$", "redirect", name="portafolio-redirect"),
    url(r"^detail/(?P<slug>[-\w]+)/$", "proyect", name="portafolio-proyect"),
)

