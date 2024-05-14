from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from user.seralizers import UserRegisterSerializer,UserSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token


# Create your views here.

class UserRegisterAPIView(APIView):
    # permission_classes = [AllowAny]
    def post(self, request):
        requested_data = request.data
        if User.objects.filter(username=requested_data.get('username')).exists():
            return Response({'massage' : 'User already exists', 'status' : False},status=status.HTTP_302_FOUND)
        serializer = UserRegisterSerializer(data=requested_data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.create(validated_data=requested_data)
            user = User.objects.get(username = serializer.data['username'])
            token_obj , _ = Token.objects.get_or_create(user=user)

            return Response({'massage' : 'User created successfully', 'token' : str(token_obj), 'status' : True}, status=status.HTTP_201_CREATED)
        else:
            return Response({'massage' : 'User already register', 'status' : False}, status=status.HTTP_302_FOUND)    
            
            

class UserAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]
    
    def delete(self, request, pk=None):
        try:
            user = get_object_or_404(User, pk=pk)            
            user.delete()
            return Response({'massage' : 'Success', 'status' : True}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'massage' : 'Data DoesNotExist'})
        
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User,pk=pk)
            serializer = UserSerializer(user)
            return Response({'massage' : 'success', 'data' : serializer.data}, status=status.HTTP_200_OK)
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({'massage' : 'success', 'data' : serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'massage' : 'success', 'data' : serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'errors' : serializer.errors, 'massage' : 'Data not found'}, status=status.HTTP_400_BAD_REQUEST)