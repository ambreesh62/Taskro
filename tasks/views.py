from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from tasks.models import Sub_Task, Task
from tasks.seralizers import Sub_TaskSerializer, TaskSerializer

# Create your views here.

class Sub_TaskAPIView(APIView):
    def post(self, request):
        serializer = Sub_TaskSerializer(data=request.data)
        
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'errors' : serializer.errors, 'massage' : 'somthing went worng'},status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({'massage' : 'Your data saved', 'data' : serializer.data}, status=status.HTTP_201_CREATED)
    
    def get(self, request, pk=None):
        try:
            if pk:
                sub_tasks = Sub_Task.objects.get(id=pk)
                serializer = Sub_TaskSerializer(sub_tasks)
                return Response({'Playload' : serializer.data, 'massage' : 'success'}, status=status.HTTP_202_ACCEPTED)
            
            sub_tasks = Sub_Task.objects.all()
            serializer = Sub_TaskSerializer(sub_tasks,many=True)
            return Response({'Playload' : serializer.data, 'massage' : 'success'}, status=status.HTTP_202_ACCEPTED)
        
        except Sub_Task.DoesNotExist:
            return Response({'massage' : 'Your data DoesNotExist'},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        try: 
            if pk:
                sub_tasks = Sub_Task.objects.get(pk=pk)
                serializer = Sub_TaskSerializer(sub_tasks, data=request.data)
                
                if not serializer.is_valid():
                    print(serializer.errors)
                    return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response({'Playload' : serializer.data, 'massage' : 'Your data is up to date'}, status=status.HTTP_201_CREATED)
        except Sub_Task.DoesNotExist:
            return Response({'massage' : 'Your data DoesNotExist'},status=status.HTTP_400_BAD_REQUEST)
            
        
    def patch(self, request, pk=None):
        try:
        
            if pk:
                sub_tasks = Sub_Task.objects.get(pk=pk)
                serializer = Sub_TaskSerializer(sub_tasks, data=request.data, partial=True)
                
                if not serializer.is_valid():
                    print(serializer.errors)
                    return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response({'Playload' : serializer.data, 'massage' : 'Data is up to date'}, status=status.HTTP_201_CREATED) 
        except Sub_Task.DoesNotExist:
            return Response({'massage' : 'Data DoesNotExist'},status=status.HTTP_400_BAD_REQUEST)        
        
    def delete(self, request, pk=None):
        try:
            if pk:
                sub_tasks = Sub_Task.objects.get(pk=pk)
                sub_tasks.delete()
                return Response({'massage' : 'Data has been deleted'}, status=status.HTTP_200_OK)
        except Sub_Task.DoesNotExist:
            return Response({'massage' : 'Data DoesNotExist'},status=status.HTTP_400_BAD_REQUEST)        


class TaskAPIView(APIView):
    def get(self, request, pk=None):
        try:
            if pk:
                tasks = Task.objects.get(id=pk)
                serializer = TaskSerializer(tasks)
                return Response({'Playload' : serializer.data, 'massage' : 'success'}, status=status.HTTP_202_ACCEPTED)
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response({'Playlod' : serializer.data, 'massage' : 'success'}, status=status.HTTP_202_ACCEPTED)
        except Task.DoesNotExist:
            return Response({'massage' : 'Data DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'errors' : serializer.errors, 'massage' : 'somthing went worng'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({'Playload' : serializer.data, 'massage' : 'success'}, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None):
        try:
            tasks = Task.objects.get(pk=pk)
            serializer = TaskSerializer(tasks, data=request.data)
            
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'errors' : serializer.errors, 'massage' : 'somthing went wworng'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'Playload' : serializer.data, 'massage' : 'Data is up to date'}, status=status.HTTP_201_CREATED)
        except Task.DoesNotExist:
            return Response({'errors' : 'Data DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        try:
            tasks = Task.objects.get(pk=pk)
            serializer = TaskSerializer(tasks, data=request.data, partial=True)
        
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'errors' : serializer.errors, 'massage' : 'somthing went wworng'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'Playload' : serializer.data, 'massage' : 'Data is up to date'}, status=status.HTTP_201_CREATED)
        except Task.DoesNotExist:
            return Response({'errors' : 'Data DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk=None):
        try:
            tasks = Task.objects.get(pk=pk)
            tasks.delete()
            return Response({'massage' : 'Data has been deleted'}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'massage' : 'Data DoesNotExist'})  