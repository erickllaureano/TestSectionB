from rest_framework import serializers, exceptions
from django.utils import timezone
from catalogues import models as catalog_models
from utilities import utilities_serializers
from . import models


class AssignedCarSerializer(serializers.ModelSerializer):
    idUser = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=catalog_models.Users.objects.all()
    )
    idCar = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=catalog_models.Cars.objects.all()
    )
    car = utilities_serializers.MultiSlugRelatedField(
        source='idCar',
        slug_fields=('id', 'modelo', 'marca', 'color', 'placa'),
        read_only=True
    )
    user = utilities_serializers.MultiSlugRelatedField(
        source='idUser',
        slug_fields=('id', 'name', 'age', 'username'),
        read_only=True
    )

    class Meta:
        model = models.AssignedCars
        fields = '__all__'


class UsedCarSerializer(serializers.ModelSerializer):
    idAssignedCar = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=models.AssignedCars.objects.all()
    )
    car = utilities_serializers.MultiSlugRelatedField(
        source='idAssignedCar.idCar',
        slug_fields=('id', 'modelo', 'marca', 'color', 'placa'),
        read_only=True
    )
    user = utilities_serializers.MultiSlugRelatedField(
        source='idAssignedCar.idUser',
        slug_fields=('id', 'name', 'age', 'username'),
        read_only=True
    )

    @staticmethod
    def send_error_message(message):
        raise exceptions.ValidationError(
            {
                'message': message
            }
        )

    def validate(self, attrs):
        attrs['now'] = timezone.localtime()
        diff_date = attrs['expiration'] - attrs['now']
        if diff_date.days < 0:
            self.send_error_message('Fecha anterior a la fecha actual')
        return super().validate(attrs)

    def create(self, validated_data):
        now_time = validated_data.pop('now')
        car = validated_data['idAssignedCar'].idCar
        user = validated_data['idAssignedCar'].idUser
        car_is_used = models.UsedCar.objects.filter(
            idAssignedCar__idCar=car
        ).first()
        user_whit_car = models.UsedCar.objects.filter(
            idAssignedCar__idUser=user
        ).first()
        if car_is_used:
            diff_date = now_time - car_is_used.expiration
            if diff_date.days < 0:
                # El carro aun le falta tiempo de expiracion
                self.send_error_message('El carro ya se encuentra en uso')
            else:
                models.UsedCar.objects.filter(
                    idAssignedCar__idCar=car
                ).delete()
        if user_whit_car:
            diff_date = now_time - user_whit_car.expiration
            if diff_date.days < 0:
                # Al usuario aun le falta tiempo para su expiracion
                self.send_error_message(
                    'El usuario ya tiene un carro asignado'
                )
            else:
                models.UsedCar.objects.filter(
                    idAssignedCar__idUser=user
                ).delete()
        return super().create(validated_data)

    class Meta:
        model = models.UsedCar
        fields = '__all__'
