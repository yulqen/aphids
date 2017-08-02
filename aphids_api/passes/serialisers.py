from rest_framework import serializers
from .models import Person, Pass, PassStatus


class PassStatusSerialiser(serializers.ModelSerializer):
    class Meta:
        model = PassStatus
        fields = ('__all__')


#class PassSerialiser(serializers.ModelSerializer):
#    class Meta:
#        model = Pass
#        fields = ('__all__')
#
#
#class PersonSerialiser(serializers.ModelSerializer):
#    class Meta:
#        model = Person
#        fields = ('__all__')
