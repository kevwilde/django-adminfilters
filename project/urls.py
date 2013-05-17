
from django.conf.urls.defaults import *
from django.conf import settings
from project.utils import populate_db
from django.views.generic import RedirectView

from django.contrib import admin

# TODO: need to include filter.py to execute Filter registration only once;
# is there a better way ?
from project import filters


admin.autodiscover()

# hack: populate db from here
populate_db()


urlpatterns = patterns('',
    # Example:
    # (r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$', RedirectView.as_view(url='/admin/project/country/')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
