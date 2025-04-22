from rest_framework import serializers
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_dt': {'read_only': True},
            'updated_dt': {'read_only': True},
            'deleted_dt': {'read_only': True},
        }