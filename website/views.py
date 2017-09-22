from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from website.models import CentroDeAcopio

class CentroDeAcopioList(ListView):
    model = CentroDeAcopio

class CentroDeAcopioCreate(CreateView):
    model = CentroDeAcopio
    success_url = reverse_lazy('centrodeacopio_list')
    fields = ['ciudad', 'estado',
            'centro', 'urgencia', 'direccion', 'brigadistas',
            'contacto','telefono','viveres',
            'medicamentos','herramientas',
            'ubicacion','infoAdicional']

class CentroDeAcopioUpdate(UpdateView):
    model = CentroDeAcopio
    success_url = reverse_lazy('centrodeacopio_list')
    fields = ['urgencia', 'direccion', 'brigadistas',
            'contacto','telefono','viveres',
            'medicamentos','herramientas',
            'ubicacion','infoAdicional']

class CentroDeAcopioDelete(DeleteView):
    model = CentroDeAcopio
    success_url = reverse_lazy('centrodeacopio_list')

class CentroDeAcopioDetail(DetailView):
    model = CentroDeAcopio

    def get_context_data(self, **kwargs):
        context = super(CentroDeAcopioDetail, self).get_context_data(**kwargs)
        return context
