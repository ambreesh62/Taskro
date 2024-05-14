from rest_framework import serializers
from user.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)  

    class Meta:
        model = User
        # fields = '__all__' 
        fields = ['username', 'password']
    
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
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.role_title = validated_data.get('role_title', instance.role_title)
        instance.dept = validated_data.get('dept', instance.dept)
        instance.location = validated_data.get('location', instance.location)
        instance.employee_no = validated_data.get('employee_no', instance.employee_no)
        
        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance  