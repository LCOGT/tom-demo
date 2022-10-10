from tom_common.mixins import SuperuserRequiredMixin
from tom_observations.views import ObservationCreateView


class CustomObservationCreateView(SuperuserRequiredMixin, ObservationCreateView):
    pass
