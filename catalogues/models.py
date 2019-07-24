from django.db import models


class Users(models.Model):
    name = models.CharField(
        max_length=100
    )
    age = models.PositiveIntegerField()

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return self.name


class Cars(models.Model):
    modelo = models.CharField(
        max_length=50
    )
    marca = models.CharField(
        max_length=50
    )
    color = models.CharField(
        max_length=50
    )
    placa = models.CharField(
        max_length=10,
        unique=True
    )

    class Meta:
        db_table = 'Cars'

    def __str__(self):
        return '' + str(self.modelo) + ' - ' + str(self.placa)
