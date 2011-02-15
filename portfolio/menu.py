from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from plugins.portafolio.models import Client

class PortaFolioMenu(Menu):
    def get_nodes(self,request):
        clients = Client.objects.all()
        assert False, [ NavigationNode( i.name, "/%s/" % i.name, i.id ) for i in clients ]

