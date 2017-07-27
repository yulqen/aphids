import datetime
from django.core.management.base import BaseCommand
import uuid as uuid_lib

from aphids_api.passes.models import Pass, Site, PassStatus, Person, Vetting


class Command(BaseCommand):
    args = ''
    help = 'Populate the database with test data.'

    def _create_pass(self):
        pass1 = Pass(
            uuid=uuid_lib.uuid4(),
            site_id=1,
            pass_issuer=1,
            holder=2,
            application_succeeded=True,
            holder_staff_number="STAFFNO001",
            application_status=1,
            proof_of_id_provided=True,
            proof_of_id_type=1,
            pass_status=1,
            application_date=datetime.date.today(),
            activation_date=datetime.date.today(),
            expiry_date=datetime.date(2018,5,1),
            termination_date=datetime.date(2017,2,3),
            withdrawn_routine=True,
            withdrawn_date=None,
            withdrawn_denied=False,
            withdrawn_denied_date=None,
            withdrawn_denied_disc_type=None,
            withdrawn_denied_comments=""
        )
        pass1.save()

    def _create_pass_status(self):
        ps1 = PassStatus(pass_status="Granted")
        ps1.save()

    def _create_person(self):
        person1 = Person(
            role=1,
            first_name="Stanley",
            middle_names="Hector Larry",
            surname="McKinley-Haberdash",
            dob=datetime.date(1921,3,15),
            place_of_birth="Stanning Layby",
            address=1,
            nationality="British",
            passport_no="123332323",
            driving_license_no="332244422",
            nat_ins="JH 23 23 14D",
            employer=1,
            employed_since=datetime.date(2014, 2, 10),
            line_manager=3,
            telecoms=1,
            biometrics=1,
            vetting_type=1,
            vetting_start=datetime.date(2015,10,2),
            vetting_ref="ABC10",
            vetting_expiry=datetime.date(2022,1,1),
            vetting_terminated=False,
            vetting_terminated_comment="Not terminated.... Yet."
        )
        person1.save()

    def _create_vetting(self):
        v1 = Vetting(
            level="CTO",
            issuing_authority=2
        )
        v2 = Vetting(
            level="ST",
            issuing_authority=2
        )
        v3 = Vetting(
            level="EXTENDED",
            issuing_authority=2
        )
        v1.save()
        v2.save()
        v3.save()


    def _create_site(self):
        site1 = Site(
            name="Major Site",
            site_type=1,
            owning_comp=1,
            managing_comp=1
        )
        site1.save()

    def handle(self, *args, **options):
        self._create_vetting()
        self._create_person()
        self._create_pass_status()
        self._create_site()
        self._create_pass()
