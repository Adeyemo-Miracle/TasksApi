# from django.shortcuts import render
# from django.http import HttpResponse
from .serializers import taskSerializers
from .models import Tasks
from rest_framework.decorators import api_view
from rest_framework.response import Response

from taskApi import serializers

# Create your views here.

@api_view(['GET'])
def tasks (request):
    task = Tasks.objects.all()
    serialized = taskSerializers(task, many=True)
    return Response (serialized.data)

@api_view(['GET'])
def task(request, pk):
    task = Tasks.objects.get(id=pk)
    serialized = taskSerializers(task, many=False)
    return Response (serialized.data)

@api_view(['POST'])
def addTasks(request):
    record = taskSerializers( data= request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)

@api_view(['PUT'])
def EditTask(request, pk):
    task = Tasks.objects.get(id=pk)
    serialized = taskSerializers(instance=task, data=request.data)
    if serialized.is_valid():
        serialized.save()
    return Response('Task has been Edited successfully')

@api_view(['DELETE'])
def deleteTasks(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()
    return Response('Task has been deleted')