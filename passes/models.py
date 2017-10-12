import uuid as uuid_lib

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Pass(models.Model):
    uuid = models.UUIDField(
        db_index=True, default=uuid_lib.uuid4, editable=False)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    pass_issuer = models.ForeignKey(
        'Person', on_delete=models.CASCADE, related_name='passes_issued')
    holder = models.ForeignKey(
        'Person', on_delete=models.CASCADE, related_name='passes')
    application_succeeded = models.BooleanField()
    holder_staff_number = models.CharField(max_length=20)
    application_status = models.ForeignKey(
        'ApplicationStatus', on_delete=models.CASCADE)
    proof_of_id_provided = models.BooleanField()
    proof_of_id_type = models.ForeignKey(
        'ProofIdType', on_delete=models.CASCADE)
    pass_privileges = models.ManyToManyField('PassPrivilege')
    pass_status = models.ForeignKey('PassStatus', on_delete=models.CASCADE)
    application_date = models.DateField()
    activation_date = models.DateField()
    expiry_date = models.DateField()
    termination_date = models.DateField()
    withdrawn_routine = models.BooleanField()
    withdrawn_date = models.DateField(null=True)
    withdrawn_denied = models.BooleanField()
    withdrawn_denied_date = models.DateField(null=True)
    withdrawn_denied_disc_type = models.ForeignKey(
        'DiscType', on_delete=models.CASCADE, null=True)
    withdrawn_denied_comments = models.TextField(null=True)

    def __str__(self):
        return f"Site: {self.site} | Holder: {self.holder}"


class PassType(models.Model):
    pass_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.pass_type}"


class PassStatus(models.Model):
    pass_status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.pass_status}"


class Person(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    middle_names = models.CharField(max_length=20, blank=True)
    surname = models.CharField(max_length=20)
    previous_surname = models.CharField(max_length=50, blank=True)
    dob = models.DateField()
    place_of_birth = models.CharField(max_length=20)
    country_of_birth = models.CharField(max_length=50)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    nationality = models.CharField(max_length=20)
    passport_no = models.CharField(max_length=20)
    driving_license_no = models.CharField(max_length=20)
    nat_ins = models.CharField(max_length=20)
    employer = models.ForeignKey('Organisation', on_delete=models.CASCADE)
    employed_since = models.DateField()
    line_manager = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, blank=True)
    telecoms = models.ForeignKey('Telecoms', on_delete=models.CASCADE)
    biometrics = models.ForeignKey('Biometrics', on_delete=models.CASCADE)
    vetting_type = models.ForeignKey('Vetting', on_delete=models.CASCADE)
    vetting_start = models.DateField()
    vetting_ref = models.CharField(max_length=20)
    vetting_expiry = models.DateField()
    vetting_terminated = models.BooleanField(blank=True)
    vetting_terminated_comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_names} {self.surname}"


class Vetting(models.Model):
    level = models.CharField(max_length=20)
    issuing_authority = models.ForeignKey('Organisation', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.level}"


class Biometrics(models.Model):
    desc = models.TextField()

    def __str__(self):
        return f"{self.desc}"


class Role(models.Model):
    role = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.role}"


class DiscType(models.Model):
    disc_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.disc_type}"


class PassPrivilege(models.Model):
    area_allowed = models.ForeignKey(
        'Area', on_delete=models.CASCADE, related_name="privileges_allowed")
    area_disallowed = models.ForeignKey(
        'Area', on_delete=models.CASCADE, related_name="privileges_disallowed")
    access_to_aircraft = models.BooleanField()
    daytime_restrictions = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.area_allowed}"


class Area(models.Model):
    name = models.CharField(max_length=20)
    sensitive = models.BooleanField()
    site = models.ForeignKey('Site', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class ProofIdType(models.Model):
    proof_id_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.proof_id_type}"


class ApplicationStatus(models.Model):
    status = models.CharField(max_length=20)
    urgency = models.IntegerField()

    def __str__(self):
        return f"{self.status}"


class Site(models.Model):
    name = models.CharField(max_length=20)
    site_type = models.ForeignKey('SiteType', on_delete=models.CASCADE)
    owning_comp = models.ForeignKey(
        'Organisation', on_delete=models.CASCADE, related_name="sites_owned")
    managing_comp = models.ForeignKey(
        'Organisation', on_delete=models.CASCADE, related_name="sites_managed")

    def __str__(self):
        return f"{self.name}"


class Organisation(models.Model):
    org_type = models.ForeignKey('OrgType', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    telecoms = models.ForeignKey('Telecoms', on_delete=models.CASCADE)
    companies_hse_reg = models.CharField(max_length=20)
    hmrc_reg = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Telecoms(models.Model):
    landline = models.CharField(max_length=20)
    mobile1 = models.CharField(max_length=20)
    mobile2 = models.CharField(max_length=20)
    email1 = models.EmailField()
    email2 = models.EmailField()

    def __str__(self):
        return f"Phone: {self.landline}"


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
    previous_address = models.ForeignKey('Address', null=True)

    def __str__(self):
        return f"{self.address1} | {self.postal_town}"


class OrgType(models.Model):
    org_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.org_type}"


class SiteType(models.Model):
    site_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.site_type}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
