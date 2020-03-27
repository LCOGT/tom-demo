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
            ),
            AccordionGroup('How It\'s Done',
                HTML(
                    """
                    <p>The first thing that was done was including bootstrap.min.js in the static files of your TOM.
                    The bootstrap files can be downloaded from 
                    <a href="https://github.com/twbs/bootstrap/releases/download/v4.4.1/bootstrap-4.4.1-dist.zip">
                    the bootstrap website. Just extract the zip, and add the file to the <code>static</code>
                    directory in your TOM.</a></p>
                    
                    <p>Next, a custom facility module was created. The module has two classes, <code>CustomLCO</code>
                    and <code>CustomLCOObservationForm</code>, both of which inherit from their LCO counterparts. You 
                    can see what methods were overridden 
                    <a href="https://github.com/LCOGT/tom-demo/commit/2120934034eef07765f969943ce5ce7760a0adc4">here.
                    </a></p>
                    
                    <p>Finally, <a href="https://django-crispy-forms.readthedocs.io/en/latest/index.html">
                    django-crispy-forms</a> were used to render the form as an <code>AccordionGroup</code></p>

                    <p>If you'd like to read more, a more detailed tutorial can be found in the 
                    <a href="https://tom-toolkit.readthedocs.io/en/stable/customization/customize_observations.html">
                    TOM Toolkit documentation</a></p>
                    """
                )
            )
        )


class CustomLCO(LCOFacility):
    observation_types = [('IMAGING', 'Imaging')]

    def get_form(self, observation_type):
        return CustomLCOObservationForm