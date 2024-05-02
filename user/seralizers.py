from rest_framework import serializers
from user.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = "__all__"
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = "__all__"