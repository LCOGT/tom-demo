from tom_observations.facilities.lco import LCOImagingObservationForm, LCOFacility


class RestrictedLCOObservationForm(LCOImagingObservationForm):
    def proposal_choices(self):
        return [('TOM demo scheduler', 'TOM Demo')]


class RestrictedLCOFacility(LCOFacility):
    observation_forms = {
        'Demo': RestrictedLCOObservationForm
    }
