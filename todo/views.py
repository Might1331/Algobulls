from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todo.serializers import taskSerializers
from todo.models import Task

@api_view(['GET'])
def home(request):
    api_urls={
        'List One Task':'/read',
        'List All Task':'/read_one/<str:pk>',
        'Create Task':'/create',
        'Update Task':'/update/<str:pk>',
        'Delete Task':'/delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def read(request):
    tasks=Task.objects.all()
    serialized=taskSerializers(tasks,many=True)
    return Response(serialized.data)

@api_view(['GET'])
def readOne(request,pk):
    tasks=Task.objects.get(id=pk)
    serialized=taskSerializers(tasks)
    return Response(serialized.data)

@api_view(['POST'])
def create(request):
    if('Tags' in request.data):
        tags=request.data["Tags"]
        tags=tags.split(',')
        tags=set(tags)
        tags=list(tags)
        request.data['Tags']=','.join([str(elem) for elem in tags])
    serialized=taskSerializers(data=request.data)

    if(serialized.is_valid()):
        serialized.save()
    else:
        print(serialized.errors)
    return Response(serialized.data)

@api_view(['POST'])
def update(request,pk):
    tasks=Task.objects.get(id=pk)
    
    if('Tags' in request.data):
        tags=request.data["Tags"]
        tags=tags.split(',')
        tags=set(tags)
        tags=list(tags)
        request.data['Tags']=','.join([str(elem) for elem in tags])

    serialized=taskSerializers(instance=tasks,data=request.data)
    if(serialized.is_valid()):
        serialized.save()
    return Response(serialized.data)

@api_view(['DELETE'])
def delete(request,pk):
    tasks=Task.objects.get(id=pk)
    tasks.delete()
    return Response("Task Deleted")

