from crispy_forms.bootstrap import Accordion, AccordionGroup
from crispy_forms.layout import Div, HTML, Layout
from django import forms

from tom_observations.facility import GenericObservationFacility, GenericObservationForm
from tom_observations.facilities.lco import LCOFacility


end_help = """
    Try the
    <a href="https://lco.global/observatory/visibility/">
        Target Visibility Calculator.
    </a>
"""


class CustomLCOObservationForm(GenericObservationForm):
    name = forms.CharField()
    ipp_value = forms.ChoiceField(label='Intra Proposal Priority (IPP factor',
                                  choices=((0.5, '0.5'), (1.0, '1.0'), (1.5, '1.5'), (2.0, '2.0')))
    exposure_count = forms.IntegerField(min_value=1)
    exposure_time = forms.FloatField(min_value=0.1)
    max_airmass = forms.FloatField()
    proposal = forms.ChoiceField(choices=[('LCOEngineering', 'LCOEngineering (LCOEngineering)')])
    filter = forms.ChoiceField(
        choices=[('R', 'Bessell-R'), ('B', 'Bessell-B'), ('V', 'Bessell-V'), ('I', 'Bessell-I'), ('air', 'Clear')]
    )
    instrument_type = forms.ChoiceField(
        choices=[('2M0-SPECTRAL-AG', '2.0 meter Spectral AG'), ('1M0-SCICAM-SINISTRO', '1.0 meter Sinistro')]
    )
    start = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))
    end = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}), help_text=end_help)
    observation_mode = forms.ChoiceField(
        choices=(('NORMAL', 'Normal'), ('TARGET_OF_OPPORTUNITY', 'Rapid Response'))
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            self.common_layout,
            self.layout()
        )

    def proposal_choices(self):
        return [('LCOEngineering', 'LCOEngineering (LCOEngineering)')]

    def instrument_choices(self):
        return [('2M0-SPECTRAL-AG', '2.0 meter Spectral AG'), ('1M0-SCICAM-SINISTRO', '1.0 meter Sinistro')]

    def filter_choices(self):
        return [('R', 'Bessell-R'), ('B', 'Bessell-B'), ('V', 'Bessell-V'), ('I', 'Bessell-I'), ('air', 'Clear')]

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
            ),
            AccordionGroup('How It\'s Done',
                HTML(
                    """
                    <p>The first thing that was done was including bootstrap.min.js in the static files of your TOM.
                    The bootstrap files can be downloaded from the 
                    <a href="https://github.com/twbs/bootstrap/releases/download/v4.4.1/bootstrap-4.4.1-dist.zip">
                    bootstrap website.</a> Just extract the zip, and add the file to the <code>static</code>
                    directory in your TOM.</p>
                    
                    <p>Next, a custom facility module was created. The module has two classes, <code>CustomLCO</code>
                    and <code>CustomLCOObservationForm</code>, both of which inherit from Toolkit interfaces in 
                    <code>facility.py</code>. You can see what methods were overridden 
                    <a href="https://github.com/LCOGT/tom-demo/commit/2120934034eef07765f969943ce5ce7760a0adc4">here.
                    </a></p>
                    
                    <p>To make the accordion, <a href="https://django-crispy-forms.readthedocs.io/en/latest/index.html">
                    django-crispy-forms</a> were used to render the form as an <code>AccordionGroup.</code></p>

                    <p>Finally, a templatetag was created to render the form, and added to the overridden 
                    <code>target_detail.html</code>.

                    <p>If you'd like to read more, a more detailed tutorial can be found in the 
                    <a href="https://tom-toolkit.readthedocs.io/en/stable/customization/customize_observations.html">
                    TOM Toolkit documentation</a></p>
                    """
                )
            )
        )

    def is_valid(self):
        self.add_error(None, 'This TOM is just for demonstration--submissions are not permitted.')
        return False

    def observation_payload(self):
        return {}

class CustomLCO(GenericObservationFacility):
    name = 'LCO Photometry'
    observation_types = [('IMAGING', 'Imaging')]

    SITES = {
        'Siding Spring': {
            'sitecode': 'coj',
            'latitude': -31.272,
            'longitude': 149.07,
            'elevation': 1116
        },
        'Sutherland': {
            'sitecode': 'cpt',
            'latitude': -32.38,
            'longitude': 20.81,
            'elevation': 1804
        },
        'Teide': {
            'sitecode': 'tfn',
            'latitude': 20.3,
            'longitude': -16.511,
            'elevation': 2390
        },
        'Cerro Tololo': {
            'sitecode': 'lsc',
            'latitude': -30.167,
            'longitude': -70.804,
            'elevation': 2198
        },
        'McDonald': {
            'sitecode': 'elp',
            'latitude': 30.679,
            'longitude': -104.015,
            'elevation': 2027
        },
        'Haleakala': {
            'sitecode': 'ogg',
            'latitude': 20.706,
            'longitude': -156.258,
            'elevation': 3065
        }
    }

    def get_form(self, observation_type):
        return CustomLCOObservationForm

    def submit_observation(self, observation_payload):
        return []

    def validate_observation(self, observation_payload):
        return []

    def data_products(self):
        return []

    def get_observation_status(self):
        return ''

    def get_observation_url(self):
        return ''

    def get_observing_sites(self):
        return self.SITES

    def get_terminal_observing_states(self):
        return ['']