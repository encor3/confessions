from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'confesionsapp.views.home', name='home'),
    url(r'^', include('confess.urls')),
    url(r'^', include('likes.urls')),


    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
