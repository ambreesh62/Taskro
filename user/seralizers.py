from rest_framework import serializers
from user.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        return user    



        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 
        
    def update(self, instance, validated_data):
        password = validated_data.get('password', instance.password)
        if password:
            instance.set_password(password)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('lastname', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get(instance.name)
        instance.role_title = validated_data.get(instance.role_title)    
        instance.dept = validated_data.get(instance.dept)
        instance.location = validated_data.get(instance.location)
        instance.employee_no =validated_data.get(instance.employee_no)
        instance.save()
        return instance        