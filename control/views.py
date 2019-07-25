from rest_framework import viewsets, exceptions
from rest_framework.response import Response
from . import models
from . import serializers
from catalogues import models as catalogues_models


class AssignedCarsView(viewsets.ModelViewSet):
    serializer_class = serializers.AssignedCarSerializer
    queryset = models.AssignedCars.objects.all()

    def retrieve(self, request, *args, **kwargs):
        try:
            user = catalogues_models.Users.objects.get(
                pk=self.kwargs.get('pk')
            )
        except catalogues_models.Users.DoesNotExist:
            raise exceptions.NotFound({'message': 'El usuario no existe'})
        instance = models.AssignedCars.objects.filter(
            idUser=user
        )
        response = serializers.AssignedCarSerializer(
            instance,
            many=True
        )
        return Response(response.data)


class UsedCarsView(viewsets.ModelViewSet):
    serializer_class = serializers.UsedCarSerializer
    queryset = models.UsedCar.objects.all()
