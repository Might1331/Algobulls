from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from todo.serializers import *
from todo.models import Task
from rest_framework.authtoken.models import Token

class register_user(APIView):
    def post(self,request):
        serializer= UserSerializer(data=request.data)
        if not serializer.is_valid():
            return {'status':403,'errors':serializer.errors}
        
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)
            
        return Response({'status':200,'payload':serializer.data,'token':str(token_obj)})


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes
from datetime import datetime

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def read(request):
    tasks=Task.objects.all()
    serialized=taskSerializers(tasks,many=True)
    return Response(serialized.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def readOne(request,pk):
    tasks=Task.objects.get(id=pk)
    serialized=taskSerializers(tasks)
    return Response(serialized.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    if('Tags' in request.data):
        tags=request.data["Tags"]
        tags=tags.split(',')
        tags=set(tags)
        tags=list(tags)
        request.data['Tags']=','.join([str(elem) for elem in tags])
        
    serialized=taskSerializers(data=request.data)
    print(request.data['Due_date'])
    if(request.data['Due_date'] and datetime.strptime(request.data['Due_date'],'%Y-%m-%d')<datetime.now()):
        return Response({'Status':400,'message':"Invalid Due Date"})
    
    if(serialized.is_valid()):
        serialized.save()
    
    return Response(serialized.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update(request,pk):
    tasks=Task.objects.get(id=pk)
    
    print(request.user, ('Timestamp' in request.data))
    if( (request.user.is_superuser==False) and ('Timestamp' in request.data)):
        return Response({'status':403,'message':'User cannot modify timestamps'})
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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete(request,pk):
    tasks=Task.objects.get(id=pk)
    tasks.delete()
    return Response("Task Deleted")

