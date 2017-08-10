from passes.models import PassStatus
from passes.serialisers import PassStatusSerialiser
from rest_framework import mixins
from rest_framework import generics


class PassStatusList(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    """
    List of pass status objects, or create new pass status.
    """
    queryset = PassStatus.objects.all()
    serializer_class = PassStatusSerialiser

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PassStatusDetail(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = PassStatus.objects.all()
    serializer_class = PassStatusSerialiser

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

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
