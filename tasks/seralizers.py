from rest_framework import serializers
from tasks.models import Sub_Task, Task

class Sub_TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Task
        fields = "__all__"



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
