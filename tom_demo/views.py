from django.views.generic import TemplateView

from tom_common.mixins import SuperuserRequiredMixin
from tom_observations.views import ObservationCreateView
from tom_superevents.models import Superevent


class CustomObservationCreateView(SuperuserRequiredMixin, ObservationCreateView):
    pass


class SupereventView(TemplateView):
    template_name = 'superevent_vue_app.html'

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        superevent = Superevent.objects.get(pk=kwargs['pk'])
        print(superevent)
        context['superevent_identifier'] = superevent.superevent_id
        return context
