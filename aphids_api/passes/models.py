import uuid as uuid_lib

from django.db import models


class Pass(models.Model):
    uuid = models.UUIDField(
        db_index=True, default=uuid_lib.uuid4, editable=False)
    site_id = models.ForeignKey('Site', on_delete=models.CASCADE)
    pass_issuer = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='passes_issued')
    holder = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='passes')
    application_succeeded = models.BooleanField()
    holder_staff_number = models.CharField(max_length=20)
    application_status = models.ForeignKey('ApplicationStatus', on_delete=models.CASCADE)
    proof_of_id_provided = models.BooleanField()
    proof_of_id_type = models.ForeignKey('ProofIdType', on_delete=models.CASCADE)
    pass_privileges = models.ManyToManyField('PassPrivilege')
    pass_status = models.ForeignKey('PassStatus', on_delete=models.CASCADE)
    application_date = models.DateField()
    activation_date = models.DateField()
    expiry_date = models.DateField()
    termination_date = models.DateField()
    withdrawn_routine = models.BooleanField()
    withdrawn_date = models.DateField()
    withdrawn_denied = models.BooleanField()
    withdrawn_denied_date = models.DateField()
    withdrawn_denied_disc_type = models.ForeignKey('DiscType', on_delete=models.CASCADE)
    withdrawn_denied_comments = models.TextField()


class PassStatus(models.Model):
    pass_status = models.CharField(max_length=20)


class Person(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    middle_names = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    dob = models.DateField()
    place_of_birth = models.CharField(max_length=20)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    nationality = models.CharField(max_length=20)
    passport_no = models.CharField(max_length=20)
    passport_image = models.BinaryField()
    driving_license_no = models.CharField(max_length=20)
    nat_ins = models.CharField(max_length=20)
    employer = models.ForeignKey('Organisation', on_delete=models.CASCADE)
    employed_since = models.DateField()
    line_manager = models.ForeignKey('Person', on_delete=models.CASCADE)
    telecoms = models.ForeignKey('Telecoms', on_delete=models.CASCADE)
    biometrics = models.ForeignKey('Biometrics', on_delete=models.CASCADE)
    vetting_type = models.ForeignKey('Vetting', on_delete=models.CASCADE)
    vetting_start = models.DateField()
    vetting_ref = models.CharField(max_length=20)
    vetting_expiry = models.DateField()
    vetting_terminated = models.BooleanField()
    vetting_terminated_comment = models.TextField()


class Vetting(models.Model):
    level = models.CharField(max_length=20)
    issuing_authority = models.ForeignKey('Organisation', on_delete=models.CASCADE)


class Biometrics(models.Model):
    desc = models.TextField()


class Role(models.Model):
    role = models.CharField(max_length=20)


class DiscType(models.Model):
    disc_type = models.CharField(max_length=20)


class PassPrivilege(models.Model):
    area_allowed = models.ForeignKey(
        'Area', on_delete=models.CASCADE, related_name="privileges_allowed")
    area_disallowed = models.ForeignKey(
        'Area', on_delete=models.CASCADE, related_name="privileges_disallowed")
    access_to_aircraft = models.BooleanField()
    daytime_restrictions = models.CharField(max_length=20)


class Area(models.Model):
    name = models.CharField(max_length=20)
    sensitive = models.BooleanField()
    site = models.ForeignKey('Site', on_delete=models.CASCADE)


class ProofIdType(models.Model):
    proof_id_type = models.CharField(max_length=20)


class ApplicationStatus(models.Model):
    status = models.CharField(max_length=20)
    urgency = models.IntegerField()


class Site(models.Model):
    name = models.CharField(max_length=20)
    site_type = models.ForeignKey('SiteType', on_delete=models.CASCADE)
    owning_comp = models.ForeignKey(
        'Organisation', on_delete=models.CASCADE, related_name="sites_owned")
    managing_comp = models.ForeignKey(
        'Organisation', on_delete=models.CASCADE, related_name="sites_managed")


class Organisation(models.Model):
    org_type = models.ForeignKey('OrgType', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    telecoms = models.ForeignKey('Telecoms', on_delete=models.CASCADE)
    companies_hse_reg = models.CharField(max_length=20)
    hmrc_reg = models.CharField(max_length=20)


class Telecoms(models.Model):
    landline = models.CharField(max_length=20)
    mobile1 = models.CharField(max_length=20)
    mobile2 = models.CharField(max_length=20)
    email1 = models.EmailField()
    email2 = models.EmailField()


class Address(models.Model):
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    address3 = models.CharField(max_length=20)
    address4 = models.CharField(max_length=20)
    postal_town = models.CharField(max_length=20)
    postal_region = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    since = models.DateField()
    previous_address = models.ForeignKey('Address')


class OrgType(models.Model):
    org_type = models.CharField(max_length=20)


class SiteType(models.Model):
    site_type = models.CharField(max_length=20)
