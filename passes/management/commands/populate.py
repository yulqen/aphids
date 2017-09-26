import datetime
from django.core.management.base import BaseCommand
import uuid as uuid_lib

from ...models import Pass, Site, PassStatus, Person, Vetting, Biometrics, Role, DiscType, PassPrivilege, \
    Area, ProofIdType, ApplicationStatus, Organisation, Telecoms, Address, OrgType, SiteType, PassType


class Command(BaseCommand):
    args = ''
    help = 'Populate the database with test data.'

    def _create_pass_type(self):
        pt1 = PassType(pass_type="Gold Pass")
        pt2 = PassType(pass_type="Silver Pass")
        pt3 = PassType(pass_type="Bronze Pass")
        pt1.save()
        pt2.save()
        pt3.save()
        print(f"Creating {pt1}, {pt2} and {pt3}")

    def _create_pass(self):
        sit1 = Site.objects.get(pk=1)
        pi1 = Person.objects.get(pk=1)
        hol1 = Person.objects.get(pk=2)
        as1 = ApplicationStatus.objects.get(pk=1)
        pid1 = ProofIdType.objects.get(pk=1)
        ps1 = PassStatus.objects.get(pk=1)
        pass1 = Pass(
            uuid=uuid_lib.uuid4(),
            site=sit1,
            pass_issuer=pi1,
            holder=hol1,
            application_succeeded=True,
            holder_staff_number="STAFFNO001",
            application_status=as1,
            proof_of_id_provided=True,
            proof_of_id_type=pid1,
            pass_status=ps1,
            application_date=datetime.date.today(),
            activation_date=datetime.date.today(),
            expiry_date=datetime.date(2018, 5, 1),
            termination_date=datetime.date(2017, 2, 3),
            withdrawn_routine=True,
            withdrawn_date=None,
            withdrawn_denied=False,
            withdrawn_denied_date=None,
            withdrawn_denied_disc_type=None,
            withdrawn_denied_comments=""
        )
        pass1.save()
        print(f"Creating {pass1}")

    def _create_pass_status(self):
        ps1 = PassStatus(pass_status="Granted")
        ps2 = PassStatus(pass_status="Declined")
        ps3 = PassStatus(pass_status="In Progress")
        ps4 = PassStatus(pass_status="Considering Revocation")
        ps5 = PassStatus(pass_status="Barred")
        ps1.save()
        ps2.save()
        ps3.save()
        ps5.save()
        ps5.save()
        print(f"Creating {ps1}")
        print(f"Creating {ps2}")
        print(f"Creating {ps3}")
        print(f"Creating {ps4}")
        print(f"Creating {ps5}")

    def _create_person(self):
        role1 = Role.objects.get(pk=1)
        address1 = Address.objects.get(pk=1)
        employer1 = Organisation.objects.get(pk=1)
        telcon1 = Telecoms.objects.get(pk=1)
        bio1 = Biometrics.objects.get(pk=1)
        vet1 = Vetting.objects.get(pk=1)
        person1 = Person(
            role=role1,
            first_name="Stanley",
            middle_names="Hector Larry",
            surname="McKinley-Haberdash",
            previous_surname="Leboa",
            dob=datetime.date(1921, 3, 15),
            place_of_birth="Stanning Layby",
            country_of_birth="Bulgaria",
            address=address1,
            nationality="British",
            passport_no="123332323",
            driving_license_no="332244422",
            nat_ins="JH 23 23 14D",
            employer=employer1,
            employed_since=datetime.date(2014, 2, 10),
            line_manager=None,
            telecoms=telcon1,
            biometrics=bio1,
            vetting_type=vet1,
            vetting_start=datetime.date(2015, 10, 2),
            vetting_ref="ABC10",
            vetting_expiry=datetime.date(2022, 1, 1),
            vetting_terminated=False,
            vetting_terminated_comment="Not terminated.... Yet."
        )
        person2 = Person(
            role=role1,
            first_name="Jim",
            middle_names="Steven",
            surname="Collins",
            previous_surname="Charnock",
            dob=datetime.date(1941, 3, 15),
            place_of_birth="Chunkly Buzzard",
            country_of_birth="Lebanon",
            address=address1,
            nationality="Czech",
            passport_no="123323",
            driving_license_no="33422",
            nat_ins="JH 23 53 13D",
            employer=employer1,
            employed_since=datetime.date(2016, 1, 10),
            line_manager=None,
            telecoms=telcon1,
            biometrics=bio1,
            vetting_type=vet1,
            vetting_start=datetime.date(2013, 11, 21),
            vetting_ref="ABC10",
            vetting_expiry=datetime.date(2022, 1, 1),
            vetting_terminated=False,
            vetting_terminated_comment="Not terminated."
        )
        person1.save()
        person2.save()
        print(f"Creating {person1}")
        print(f"Creating {person2}")

    def _create_vetting(self):
        ia1 = Organisation.objects.get(pk=1)
        v1 = Vetting(
            level="CTO",
            issuing_authority=ia1
        )
        v2 = Vetting(
            level="ST",
            issuing_authority=ia1
        )
        v3 = Vetting(
            level="EXTENDED",
            issuing_authority=ia1
        )
        v1.save()
        v2.save()
        v3.save()
        print(f"Creating {v1}")
        print(f"Creating {v2}")
        print(f"Creating {v3}")

    def _create_biometrics(self):
        bm1 = Biometrics(
            desc="Biometrics description"
        )
        bm1.save()
        print(f"Creating {bm1}")


    def _create_role(self):
        role1 = Role(
            role="A Role"
        )
        role1.save()
        print(f"Creating {role1}")

    def _create_disctype(self):
        dt1 = DiscType(
            disc_type="A type of discipline"
        )
        dt1.save()
        print(f"Creating {dt1}")

    def _create_passprivilege(self):
        area = Area.objects.get(pk=1)
        area2 = Area.objects.get(pk=2)
        pp1 = PassPrivilege(
            area_allowed=area,
            area_disallowed=area2,
            access_to_aircraft=False,
            daytime_restrictions="Daytime restriction"
        )
        pp1.save()
        print(f"Creating {pp1}")

    def _create_area(self):
        site1 = Site.objects.get(pk=1)
        area1 = Area(
            name="An area",
            sensitive=True,
            site=site1
        )
        area2 = Area(
            name="An area 2",
            sensitive=True,
            site=site1
        )
        area1.save()
        area2.save()
        print(f"Creating {area1}")
        print(f"Creating {area2}")

    def _create_site(self):
        st1 = SiteType.objects.get(pk=1)
        oc = Organisation.objects.get(pk=1)
        mc = Organisation.objects.get(pk=1)
        site1 = Site(
            name="Major Site",
            site_type=st1,
            owning_comp=oc,
            managing_comp=mc
        )
        site1.save()
        print(f"Creating {site1}")

    def _create_proofidtype(self):
        pidt1 = ProofIdType(
            proof_id_type="Passport"
        )
        pidt2 = ProofIdType(
            proof_id_type="Driving License"
        )
        pidt3 = ProofIdType(
            proof_id_type="Library Card"
        )
        pidt1.save()
        pidt2.save()
        pidt3.save()
        print(f"Creating {pidt1}")
        print(f"Creating {pidt2}")
        print(f"Creating {pidt3}")

    def _create_applicationstatus(self):
        as1 = ApplicationStatus(
            status="EARLY STAGE",
            urgency=10
        )
        as2 = ApplicationStatus(
            status="FINALISED",
            urgency=10
        )
        as1.save()
        as2.save()
        print(f"Creating {as1}")
        print(f"Creating {as2}")

    def _create_organisation(self):
        orgt1 = OrgType.objects.get(pk=1)
        add1 = Address.objects.get(pk=3)
        telc1 = Telecoms.objects.get(pk=3)
        org1 = Organisation(
            org_type=orgt1,
            name="Transport Systems",
            address=add1,
            telecoms=telc1,
            companies_hse_reg="ADFDJA22332",
            hmrc_reg="FFFJF1"
        )
        org1.save()
        print(f"Creating {org1}")

    def _create_telecoms(self):
        tc1 = Telecoms(
            landline="0203 23323 323",
            mobile1="07842 232 4244",
            mobile2="07842 232 4244",
            email1="telecoms1@telecoms1.com",
            email2="telecoms2@telecoms1.com"
        )
        tc2 = Telecoms(
            landline="0203 23323 323",
            mobile1="07842 232 4244",
            mobile2="07842 232 4244",
            email1="telecoms1@telecoms2.com",
            email2="telecoms2@telecoms2.com"
        )
        tc3 = Telecoms(
            landline="0203 23323 323",
            mobile1="07842 232 4244",
            mobile2="07842 232 4244",
            email1="telecoms1@telecoms3.com",
            email2="telecoms2@telecoms3.com"
        )
        tc1.save()
        tc2.save()
        tc3.save()
        print(f"Creating{tc1}")
        print(f"Creating{tc2}")
        print(f"Creating{tc3}")

    def _create_address(self):
        ad1 = Address(
            address1="Address 1 (AD1)",
            address2="Address 2 (AD1)",
            address3="Address 3 (AD1)",
            address4="Address 4 (AD1)",
            postal_town="Town 1",
            postal_region="Region 1",
            county="County 1",
            postcode="AD1 1AA",
            since=datetime.date(2011, 1, 1),
            previous_address=None
        )
        ad2 = Address(
            address1="Address 1 (AD2)",
            address2="Address 2 (AD2)",
            address3="Address 3 (AD2)",
            address4="Address 4 (AD2)",
            postal_town="Town 2",
            postal_region="Region 2",
            county="County 2",
            postcode="AD2 2AA",
            since=datetime.date(2011, 1, 1),
            previous_address=None
        )
        ad3 = Address(
            address1="Address 1 (AD3)",
            address2="Address 2 (AD3)",
            address3="Address 3 (AD3)",
            address4="Address 4 (AD3)",
            postal_town="Town 3",
            postal_region="Region 3",
            county="County 4",
            postcode="AD3 3AA",
            since=datetime.date(2011, 1, 1),
            previous_address=None
        )
        ad1.save()
        ad2.save()
        ad3.save()
        print(f"Creating {ad1}")
        print(f"Creating {ad2}")
        print(f"Creating {ad3}")

    def _create_orgtype(self):
        orgt1 = OrgType(
            org_type="Human Resources"
        )
        orgt1.save()
        print(f"Creating {orgt1}")

    def _create_sitetype(self):
        st1 = SiteType(
            site_type="Transport Hub"
        )
        st1.save()
        print(f"Creating {st1}")

    def handle(self, *args, **options):
        self._create_address()
        self._create_telecoms()
        self._create_biometrics()
        self._create_orgtype()
        self._create_organisation()
        self._create_vetting()
        self._create_role()
        self._create_person()
        self._create_sitetype()
        self._create_applicationstatus()
        self._create_proofidtype()
        self._create_site()
        self._create_area()
        self._create_passprivilege()
        self._create_disctype()
        self._create_pass_status()
        self._create_pass()
        self._create_pass_type()
