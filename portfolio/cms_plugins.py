from models import PortfolioPlugin
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.conf import settings 
from django.utils.translation import ugettext as _

class PortfolioPluginBase(CMSPluginBase):
    model = PortfolioPlugin
    render_template = 'portfolio/portfolio.html'
    name = _("Portafolio")
    def render(self, context, instance, placeholder):
        context.update({'instance':instance,'placeholder':placeholder})
        return context

plugin_pool.register_plugin(PortfolioPluginBase)
