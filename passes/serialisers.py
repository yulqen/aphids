from rest_framework import serializers
from .models import PassStatus

from django.contrib.auth.models import User


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class PassStatusSerialiser(serializers.ModelSerializer):
    class Meta:
        model = PassStatus
        fields = ('__all__')

