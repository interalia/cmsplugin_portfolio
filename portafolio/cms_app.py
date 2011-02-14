from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class PortaFolioApp(CMSApp):
    name = u"Portafolio"
    urls = ["portafolio.urls",]

apphook_pool.register(PortaFolioApp)
