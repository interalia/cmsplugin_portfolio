from django.utils.translation import ugettext as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class PortaFolioApp(CMSApp):
    name = _("Portafolio")
    urls = ["portfolio.urls"]

apphook_pool.register(PortaFolioApp)
