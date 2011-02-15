from django.db import models
from cms.models import CMSPlugin
from django.core.exceptions import ValidationError


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
class Client(models.Model):
    name = models.CharField(max_length= 100)

    def __unicode__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.name

class Proyect(models.Model):
    service = models.ForeignKey(Service, related_name="proyects")
    country = models.ForeignKey(Country, related_name="proyects")
    client = models.ForeignKey(Client, related_name ="proyects")
    name = models.CharField(max_length= 100)
    description_short = models.TextField( help_text = u"las lineas nuevas son consideradas br tag")
    description_long  = models.TextField(help_text=u"las lineas nuevas son  consideradas br tag ")
    url = models.URLField(blank=True )
    slug = models.SlugField()
    twitter = models.CharField(max_length=20, help_text="twitt via ..", blank = True, null = True)
    facebook_like = models.URLField( blank =True, null = True)
    sequence = models.IntegerField()

    @models.permalink
    def get_absolute_url(self):
        return ("portafolio-proyect", [self.slug])
    def get_url(self):
        if "http://" in self.url:
            st = self.url.split("http://")[1]
        elif "https://" in self.url:
            st =  self.url.split("https://")[1]
        else:
            st = self.url
        if st.endswith("/"):
            st = st[:-1]
        return st
                
        
    def __unicode__(self):
        return self.name
class Image(models.Model):
    image = models.ImageField(upload_to= "uploaded_images")
    main = models.BooleanField(default =False)
    sequence = models.IntegerField()
    proyect = models.ForeignKey(Proyect, related_name="images")
    class Meta:
        ordering = ("sequence",)

class PortafolioPlugin(CMSPlugin):
    portafolio = models.ManyToManyField(Proyect)


