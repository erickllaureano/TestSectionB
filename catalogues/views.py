from rest_framework import viewsets
from . import serializers
from . import models


class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.Users.objects.all()


class CarView(viewsets.ModelViewSet):
    serializer_class = serializers.CarSerializer
    queryset = models.Cars.objects.all()
