from django import template
from django.urls import reverse

from tom_observations.facility import get_service_class


register = template.Library()


@register.inclusion_tag('demo_code/partials/observation_form.html')
def lco_observation_form(target):
    facility_class = get_service_class('LCO')()
    initial_fields = {
        'target_id': target.id,
        'facility': 'LCO',
        'observation_type': 'photometry'
    }
    obs_form = facility_class.get_form('photometry')(initial=initial_fields)
    obs_form.helper.form_action = reverse('tom_observations:create', kwargs={'facility': 'LCO'})

    return {'obs_form': obs_form}