# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username' , 'password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        return user
    