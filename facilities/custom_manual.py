import json

from django import forms
from crispy_forms.layout import Column, Div, Layout, Row

from tom_observations.facility import BaseManualObservationFacility, BaseManualObservationForm
from tom_observations.observing_strategy import GenericStrategyForm
from tom_targets.models import Target


class DemonstrationManualObservationForm(BaseManualObservationForm):
    name = forms.CharField()
    start = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}), help_text='Start date of the observation')
    end = forms.CharField(required=False, widget=forms.TextInput(attrs={'type': 'date'}), help_text='End date of the observation')
    observation_id = forms.CharField(required=False, help_text='Tracking id of the observation')
    exposure_count = forms.IntegerField(min_value=1, help_text='Exposure Count')
    exposure_time = forms.FloatField(min_value=0.1)
    max_airmass = forms.FloatField(min_value=0)
    annotations = forms.CharField(required=False, widget=forms.Textarea(), help_text='Notes about the observation')

    def layout(self):
        return Div(
            Div('name'),
            Div('observation_id'),
            Row(
                Column(
                    'start', 'exposure_count', 'max_airmass'
                ),
                Column(
                    'end', 'exposure_time'
                )
            ),
            Div(
                'annotations'
            )
        )


class DemonstrationManualObservingStrategyForm(GenericStrategyForm, DemonstrationManualObservationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['groups', 'target_id', 'name', 'start', 'end', 'observation_id', 'annotations']:
            self.fields.pop(field_name, None)
        for field in self.fields:
            if field != 'strategy_name':
                self.fields[field].required = False
        self.helper.layout = Layout(
            self.common_layout,
            self.layout()
        )


class DemonstrationManualFacility(BaseManualObservationFacility):
    name = 'Demonstration Manual Facility'
    observation_types = [('OBSERVATION', 'Photometry')]

    def get_form(self, observation_type):
        return DemonstrationManualObservationForm

    def get_strategy_form(self, observation_type):
        return DemonstrationManualObservingStrategyForm

    def get_observation_url(self, observation_id):
        return ''

    def get_observing_sites(self):
        return {}

    def get_terminal_observing_states(self):
        return []

    def submit_observation(self, observation_payload):
        obs_ids = []
        obs_params = json.loads(observation_payload['params'])

        if obs_params.get('observation_id'):
            obs_ids.append(obs_params['observation_id'])
        else:
            target = Target.objects.get(pk=observation_payload['target_id']).name
            obs_name = obs_params['name']
            facility = obs_params['facility']
            start = obs_params[self.get_start_end_keywords()[0]]

            obs_id = f'{obs_name}:{target}-{facility}-{start}'
            obs_ids.append(obs_id)

        return obs_ids

    def validate_observation(self):
        return True

    def data_products(self, observation_id, product_id=None):
        return []
