from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r"^$", "portfolio.views.index", name="portfolio-index"),
    url(r"^small/$", "portfolio.views.show_small", name="portfolio-small"),
    url(r"^redirect/$", "portfolio.views.redirect", name="portfolio-redirect"),
    url(r"^detail/(?P<slug>[-\w]+)/$", "portfolio.views.proyect", name="portfolio-proyect"),
)
