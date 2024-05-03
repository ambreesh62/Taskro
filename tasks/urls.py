from django.contrib import admin
from django.urls import path
from tasks.views import Sub_TaskAPIView

urlpatterns = [
    path('subtask', Sub_TaskAPIView.as_view()),
    path('subtask/<int:pk>/', Sub_TaskAPIView.as_view(), name='subtask-detail'),
]
