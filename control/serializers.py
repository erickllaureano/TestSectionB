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
        slug_fields=('id','modelo', 'marca', 'color', 'placa'),
        read_only=True
    )
    User = utilities_serializers.MultiSlugRelatedField(
        source='idUser',
        slug_fields=('id', 'name', 'age', 'username'),
        read_only=True
    )

    class Meta:
        model = models.AssignedCars
        fields = '__all__'
