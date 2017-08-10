from passes.models import PassStatus
from passes.serialisers import PassStatusSerialiser, UserSerialiser
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser


class UserDetail(generics.RetrieveAPIView):
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
