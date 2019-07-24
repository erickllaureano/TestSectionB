from rest_framework import serializers, exceptions
from . import models


class UserSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs['age'] < 18:
            raise exceptions.ValidationError(
                {
                    'message': 'El usuario debe ser mayor de edad'
                }
            )
        return super().validate(attrs)

    class Meta:
        model = models.Users
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cars
        fields = '__all__'
