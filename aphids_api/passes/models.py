import uuid as uuid_lib

from django.db import models
from django.urls import reverse


class Pass(models.Model):
    uuid = models.UUIDField(
        db_index=True, default=uuid_lib.uuid64, editable=False)
    site_id = models.ForeignKey('Site', on_delete=models.CASCADE)
    pass_issuer = models.ForeignObject('Person', on_delete=models.CASCADE)
    holder = models.ForeignObject('Person', on_delete=models.CASCADE)
    application_succeeded = models.BooleanField()
    holder_staff_number = models.CharField()
    application_status = models.ForeignKey('ApplicationStatus', on_delete=models.CASCADE)
    proof_of_id_provided = models.BooleanField()
    proof_of_id_type = models.ForeignKey('ProofIdType', on_delete=models.CASCADE)
    pass_privileges = models.ManyToManyField('PassPrivilege', on_delete=models.CASCADE)
    pass_status = models.ForeignKey('PassStatus', on_delete=models.CASCADE)
    application_date = models.DateField()
    activation_date = models.DateField()
    expiry_date = models.DateField()
    termination_date = models.DateField()
    withdrawn_route = models.BooleanField()
    withdrawn_date = models.DateField()
    withdrawn_denied = models.BooleanField()
    withdrawn_denied_date = models.DateField()
    withdrawn_denied_disc_type = models.ForeignKey('DiscType', on_delete=models.CASCADE)
    withdrawn_denied_comments = models.TextField()


class DiscType(models.Model):
    disc_type = models.CharField()


class PassPrivilege(models.Model):
    area_allowed = models.ForeignKey('Area', on_delete=models.CASCADE)
    area_disallowed = models.ForeignKey('Area', on_delete=models.CASCADE)
    access_to_aircraft = models.BooleanField()
    daytime_restrictions = models.CharField()


class Area(models.Model):
    name = models.CharField()
    sensitive = models.BooleanField()
    site = models.ForeignKey('Site', on_delete=models.CASCADE)


class ProofIdType(models.Model):
    pass


class ApplicationStatus(models.Model):
    pass


class Person(models.Model):
    pass


class Site(models.Model):
    name = models.CharField()
    site_type = models.ForeignKey('SiteType', on_delete=models.CASCADE)
    owning_comp = models.ForeignKey('Organisation', on_delete=models.CASCADE)
    managing_comp = models.ForeignKey('Organisation', on_delete=models.CASCADE)


class Organisation(models.Model):
    org_type = models.ForeignKey('OrgType', on_delete=models.CASCADE)
    name = models.CharField()
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    telecoms = models.ForeignKey('Telecoms', on_delete=models.CASCADE)
    companies_hse_reg = models.CharField()
    hmrc_reg = models.CharField()


class Telecoms(models.Model):
    landline = models.CharField()
    mobile1 = models.CharField()
    mobile2 = models.CharField()
    email1 = models.EmailField()
    email2 = models.EmailField()


class Address(models.Model):
    pass


class OrgType(models.Model):
    pass


class SiteType(models.Model):
    pass
