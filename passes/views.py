from passes.models import PassStatus
from passes.serialisers import PassStatusSerialiser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PassStatusList(APIView):
    """
    List of pass status objects, or create new pass status.
    """
    def get(self, request, format=None):
        ps = PassStatus.objects.all()
        serializer = PassStatusSerialiser(ps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PassStatusSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PassStatusDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return PassStatus.objects.get(pk=pk)
        except PassStatus.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        ps = self.get_object(pk)
        serializer = PassStatusSerialiser(ps)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ps = self.get_object(pk)
        serializer = PassStatusSerialiser(ps, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ps = self.get_object(pk)
        ps.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
