from crispy_forms.bootstrap import Accordion, AccordionGroup
from crispy_forms.layout import Div, HTML, Layout
from django import forms

from tom_observations.facilities.lco import LCOFacility, LCOImagingObservationForm

class CustomLCOObservationForm(LCOImagingObservationForm):
    ipp_value = forms.ChoiceField(label='Intra Proposal Priority (IPP factor',
                                  choices=((0.5, '0.5'), (1.0, '1.0'), (1.5, '1.5'), (2.0, '2.0')))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            self.common_layout,
            self.layout()
        )

    def instrument_choices(self):
        return [(k, v) for k, v in super().instrument_choices() if k in ['1M0-SCICAM-SINISTRO', '2M0-SPECTRAL-AG']]

    def filter_choices(self):
        return [(k, v) for k, v in super().filter_choices() if k in ['I', 'R', 'V', 'B', 'air']]

    def layout(self):
        return Accordion(
            AccordionGroup('Observation Details', 
                Div('name', css_class='form-row'),
                Div(
                    Div('proposal', css_class='col'),
                    Div('ipp_value', css_class='col'),
                    css_class='form-row'
                ),
            ),
            AccordionGroup('Instruments',
                Div(
                    Div('filter', css_class='col'),
                    Div('instrument_type', css_class='col'),
                    css_class='form-row'
                )
            ),
            AccordionGroup('Parameters',
                Div(
                    Div('exposure_count', 'max_airmass', css_class='col'),
                    Div('exposure_time', 'observation_mode', css_class='col'),
                    css_class='form-row'
                )
            ),
            AccordionGroup('Window',
                Div(
                    Div('start', css_class='col'),
                    Div('end', css_class='col'),
                    css_class='form-row'
                )
            )
        )


class CustomLCO(LCOFacility):
    observation_types = [('IMAGING', 'Imaging')]

    def get_form(self, observation_type):
        return CustomLCOObservationForm