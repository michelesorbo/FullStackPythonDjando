from django.contrib.sitemaps import Sitemap
from .models import Blog

#Creo le url per i post in blog
class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Blog.objects.all()
    
    def lastmod(self, obj):
        return obj.data