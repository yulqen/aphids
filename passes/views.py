from passes.models import (Pass, PassStatus, Person, ApplicationStatus, ProofIdType, PassType)
from passes.serialisers import (PassStatusSerialiser, UserSerialiser,
                                PersonSerialiser, ApplicationStatusSerialiser,
                                ProofIdTypeSerialiser, PassTypeSerialiser,
                                PassSerialiser)
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.reverse import reverse
from django.contrib.auth.models import User


@authentication_classes(['IsAuthenticatedOrReadOnly'])
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'persons': reverse('person-list', request=request, format=format),
        'application-statuses': reverse('application-status-list', request=request, format=format),
        'proofidtype': reverse('proof-id-type-list', request=request, format=format),
        'pass-statuses': reverse('pass-status-list', request=request, format=format),
        'pass-types': reverse('pass-type-list', request=request, format=format),
        'passes': reverse('pass-list', request=request, format=format),
    })


class PassDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pass.objects.all()
    serializer_class = PassSerialiser
    permission_classes = (permissions.IsAuthenticated,)


class PassList(generics.ListCreateAPIView):
    queryset = Pass.objects.all()
    serializer_class = PassSerialiser
    permission_classes = (permissions.IsAuthenticated,)


class ProofIdTypeList(generics.ListCreateAPIView):
    queryset = ProofIdType.objects.all()
    serializer_class = ProofIdTypeSerialiser
    permission_classes = (permissions.IsAuthenticated,)


class ProofIdTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProofIdType.objects.all()
    serializer_class = ProofIdTypeSerialiser
    permission_classes = (permissions.IsAuthenticated,)


class ApplicationStatusList(generics.ListCreateAPIView):
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerialiser
    permission_classes = (permissions.IsAuthenticated,)


class ApplicationStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerialiser
    permission_classes = (permissions.IsAuthenticated,)


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerialiser
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'person'


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerialiser
    permission_classes = (permissions.IsAuthenticated,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser


class PassTypeList(generics.ListCreateAPIView):
    queryset = PassType.objects.all()
    serializer_class = PassTypeSerialiser


class PassTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PassType.objects.all()
    serializer_class = PassTypeSerialiser


class PassStatusList(generics.ListCreateAPIView):
    """
    List of pass status objects, or create new pass status.
    """
    queryset = PassStatus.objects.all()
    serializer_class = PassStatusSerialiser
    permission_classes = (permissions.IsAuthenticated,)


class PassStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = PassStatus.objects.all()
    serializer_class = PassStatusSerialiser
    permission_classes = (permissions.IsAuthenticated,)
