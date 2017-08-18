from rest_framework import serializers
from .models import (PassStatus, Pass, Person, ApplicationStatus, ProofIdType,
                     PassPrivilege, DiscType)

from django.contrib.auth.models import User


class DiscTypeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = DiscType
        fields = ('__all__')


class PassPrivilegeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = PassPrivilege
        fields = ('__all__')


class ProofIdTypeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ProofIdType
        fields = ('__all__')


class ApplicationStatusSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = ('__all__')


class PersonSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')
        lookup_field = 'person'


class PassSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = ('__all__')


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class PassStatusSerialiser(serializers.ModelSerializer):
    class Meta:
        model = PassStatus
        fields = ('__all__')

