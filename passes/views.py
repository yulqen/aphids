from passes.models import (PassStatus, Person, ApplicationStatus, ProofIdType)
from passes.serialisers import (PassStatusSerialiser, UserSerialiser,
                                PersonSerialiser, ApplicationStatusSerialiser,
                                ProofIdTypeSerialiser)
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.contrib.auth.models import User


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'persons': reverse('person-list', request=request, format=format),
        'applicationstatuses': reverse('application-status-list', request=request, format=format),
        'proofidtype': reverse('proof-id-type-list', request=request, format=format),
    })


class ProofIdTypeList(generics.ListCreateAPIView):
    queryset = ProofIdType.objects.all()
    serializer_class = ProofIdTypeSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProofIdTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProofIdType.objects.all()
    serializer_class = ProofIdTypeSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ApplicationStatusList(generics.ListCreateAPIView):
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ApplicationStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser


class PassStatusList(generics.ListCreateAPIView):
    """
    List of pass status objects, or create new pass status.
    """
    queryset = PassStatus.objects.all()
    serializer_class = PassStatusSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PassStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = PassStatus.objects.all()
    serializer_class = PassStatusSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)





# OLD FUNCTION BASED VIEWS LEFT FOR POSTERITY
# @api_view(['GET', 'POST'])
# def pass_status_list(request, format=None):
#     """
#     List all pass statuses, or create a new one.
#     """
#     if request.method == 'GET':
#         ps = PassStatus.objects.all()
#         serializer = PassStatusSerialiser(ps, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = PassStatusSerialiser(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def pass_status_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a pass_status object."
#     """
#     try:
#         ps = PassStatus.objects.get(pk=pk)
#     except PassStatus.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PassStatusSerialiser(ps)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = PassStatusSerialiser(ps, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         ps.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
