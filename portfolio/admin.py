from django.contrib import admin
from django.db import models
from django.contrib import admin

from models import Service, Client, Proyect, Image, Country
from cms.plugins.text.widgets.wymeditor_widget import WYMEditor
from sorl.thumbnail.admin import AdminInlineImageMixin, AdminImageWidget
from django.conf.urls.defaults import patterns

    
class ImageInline(AdminInlineImageMixin,admin.TabularInline):
    model =Image
    def formfield_for_dbfield(self,db_field, **kwargs):
        if isinstance(db_field, models.ImageField):
            return db_field.formfield( widget = AdminImageWidget)
        return super(ImageInline, self).formfield_for_dbfield(db_field, **kwargs)


class ProyectAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    formfield_overrides = {
     #   models.TextField : {'widget': WYMEditor},
    }
    list_display = ("name", "sequence",)
    list_editable = ( "sequence", )
    search_fields = ['name']
    class Media:
        js = (
        "js/jquery-1.4.3.min.js",
        "https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js",
        "js/order.js")


admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Country)
admin.site.register(Proyect,ProyectAdmin)

