from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^website/', include('website.urls')),
    url(r'^admin/', admin.site.urls),
]
