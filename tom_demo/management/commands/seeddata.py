import json
from random import randint

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import factory

from tom_alerts.brokers.mars import MARSBroker, MARSQueryForm
from tom_catalogs.harvesters.simbad import SimbadHarvester
from tom_catalogs.harvesters.mpc import MPCHarvester
from tom_observations.models import ObservationRecord
from tom_targets.models import Target


class ObservingRecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ObservationRecord

    # target = factory.RelatedFactory(TargetFactory)
    facility = 'LCO'
    observation_id = factory.Faker('pydecimal', right_digits=0, left_digits=7)
    status = 'PENDING'
    parameters = json.dumps({
        'facility': 'LCO',
        'target_id': 1,
        'observation_type': 'IMAGING',
        'name': 'With Perms',
        'ipp_value': 1.05,
        'start': '2020-01-01T00:00:00',
        'end': '2020-01-02T00:00:00',
        'exposure_count': 1,
        'exposure_time': 2.0,
        'max_airmass': 4.0,
        'observation_mode': 'NORMAL',
        'proposal': 'LCOSchedulerTest',
        'filter': 'I',
        'instrument_type': '1M0-SCICAM-SINISTRO'
    })


def create_simbad_targets(targets):
    simbad = SimbadHarvester()
    for target in targets:
        simbad.query(target)
        try:
            simbad.to_target().save()
        except Exception:
            pass


def create_mpc_targets(targets):
    mpc = MPCHarvester()
    for target in targets:
        mpc.query(target)
        try:
            mpc.to_target().save()
        except Exception:
            pass


def create_mars_targets():
    mars_form = MARSQueryForm({
        'objectcone': 'm31,0.0125',
        'jd__gt': '2458388.5',
        'jd__lt': '2458510.5'
    })
    mars_form.is_valid()
    mars = MARSBroker()
    try:
        mars.fetch_and_save_all(mars_form.cleaned_data)
    except Exception:
        pass


def create_mock_observations():
    targets = Target.objects.all()
    for target in targets:
        for i in range(0, randint(1, 5)):
            ObservingRecordFactory.create(target_id=target.id)


def create_users():
    User.objects.create_superuser('admin', email='dcollom@lco.global', password='admin')
    User.objects.create('guest', email='dcollom@lco.global', password='guest')


class Command(BaseCommand):
    help = 'Seeds base data for TOM Demo'

    def handle(self, *args, **options):
        create_simbad_targets(['m31', 'm41', 'm51'])
        create_mpc_targets(['ceres', 'eris'])
        create_mars_targets()
        create_mock_observations()
        create_users()
