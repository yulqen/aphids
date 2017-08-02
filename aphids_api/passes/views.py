from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from passes.models import PassStatus
from passes.serialisers import PassStatusSerialiser


@csrf_exempt
def pass_status_list(request):
    """
    List all pass statuses, or create a new one.
    """
    if request.method == 'GET':
        ps = PassStatus.objects.all()
        serializer = PassStatusSerialiser(ps, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PassStatusSerialiser(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def pass_status_detail(request, pk):
    """
    Retrieve, update or delete a pass_status object."
    """
    try:
        ps = PassStatus.objects.get(pk=pk)
    except PassStatus.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PassStatusSerialiser(ps)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PassStatusSerialiser(ps, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ps.delete()
        return HttpResponse(status=204)
