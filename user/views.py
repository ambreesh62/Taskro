from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from user.seralizers import UserRegisterSerializer
from rest_framework import status


# Create your views here.

# class UserRegisterAPIView(APIView):