from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from tasks.models import Sub_Task, Task
from tasks.seralizers import Sub_TaskSerializer, TaskSerializer

# Create your views here.
