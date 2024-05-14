from django.contrib import admin
from django.urls import path, include
from user.views import UserRegisterAPIView, UserAPIView


urlpatterns = [
    path('userregister/', UserRegisterAPIView.as_view()),
    
    path('user/<int:pk>/', UserAPIView.as_view()),
    path('user/',UserAPIView.as_view()),
    path('auth/', include('rest_framework.urls'))
]
