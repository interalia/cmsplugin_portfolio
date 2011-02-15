from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r"^$", "portafolio.views.index", name="portafolio-index"),
    url(r"^small/$", "portafolio.views.show_small", name="portafolio-small"),
    url(r"^redirect/$", "portafolio.views.redirect", name="portafolio-redirect"),
    url(r"^detail/(?P<slug>[-\w]+)/$", "portafolio.views.proyect", name="portafolio-proyect"),
)
