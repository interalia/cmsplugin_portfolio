from models import PortafolioPlugin
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.conf import settings 
class PortafolioPluginBase(CMSPluginBase):
    model = PortafolioPlugin
    render_template = 'portafolio/portafolio.html'
    name = u"Portafolio"
    def render(self, context, instance, placeholder):
        context.update({'instance':instance,'placeholder':placeholder})
        return context

plugin_pool.register_plugin(PortafolioPluginBase)
