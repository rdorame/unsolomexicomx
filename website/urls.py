from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from website.models import CentroDeAcopio
from . import views

urlpatterns = [
    url(r'^$', views.CentroDeAcopioList.as_view(), name='centrodeacopio_list'),
    url(r'^registrarCentro$', views.CentroDeAcopioCreate.as_view(), name='centrodeacopio_new'),
    url(r'^editarCentro/(?P<pk>\d+)$', views.CentroDeAcopioUpdate.as_view(), name='centrodeacopio_edit'),
    url(r'^eliminarCentro/(?P<pk>\d+)$', views.CentroDeAcopioDelete.as_view(), name='centrodeacopio_delete'),
    url(r'^vercentro/(?P<pk>\d+)$', views.CentroDeAcopioDetail.as_view(), name='centrodeacopio_detail'),
]
