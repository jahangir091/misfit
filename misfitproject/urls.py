
from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

from views import IndexClass


# Setup Django Admin

admin.autodiscover()


urlpatterns = patterns('',

                        # url(r'^/?$', TemplateView.as_view(template_name='index.html'), name='home'),
                       url(r'^/?$', IndexClass.as_view(), name='home'),
                        (r"^account/", include("account.urls")),
                        (r'^admin/', include(admin.site.urls)),
                       (r'^user/', include('misfitproject.people.urls')),
                       )

