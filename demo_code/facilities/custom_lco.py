from django import forms

from tom_observations.facilities.lco import LCOFacility, LCOImagingObservationForm

class SimpleLCOObservationForm(LCOImagingObservationForm):
    ipp_value = forms.ChoiceField(label='Intra Proposal Priority (IPP factor',
                                  choices=((0.5, '0.5'), (1.0, '1.0'), (1.5, '1.5'), (2.0, '2.0')))
    max_airmass = forms.FloatField(widget=forms.HiddenInput(), initial=3)

    def instrument_choices(self):
        return [(k, v) for k, v in super().instrument_choices() if k in ['1M0-SCICAM-SINISTRO', '2M0-SPECTRAL-AG']]

    def filter_choices(self):
        return [(k, v) for k, v in super().filter_choices() if k in ['I', 'R', 'V', 'B', 'air']]


class CustomLCO(LCOFacility):
    observation_types = [('IMAGING', 'Imaging')]

    def get_form(self, observation_type):
        return SimpleLCOObservationForm