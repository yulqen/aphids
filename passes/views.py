from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from passes.models import PassStatus
from passes.serialisers import PassStatusSerialiser


@api_view(['GET', 'POST'])
def pass_status_list(request, format=None):
    """
    List all pass statuses, or create a new one.
    """
    if request.method == 'GET':
        ps = PassStatus.objects.all()
        serializer = PassStatusSerialiser(ps, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PassStatusSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def pass_status_detail(request, pk, format=None):
    """
    Retrieve, update or delete a pass_status object."
    """
    try:
        ps = PassStatus.objects.get(pk=pk)
    except PassStatus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PassStatusSerialiser(ps)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PassStatusSerialiser(ps, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ps.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
