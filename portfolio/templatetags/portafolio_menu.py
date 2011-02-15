from django import template
from portafolio.models import Client

register = template.Library()

@register.inclusion_tag("portfolio/menu.html")
def portafolio_menu_client(p):
    return {"portafolio_clients":Client.objects.all(), "actual":p}
