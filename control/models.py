from django.db import models
from catalogues import models as catalogModels


class AssignedCars(models.Model):
    idCar = models.ForeignKey(
        catalogModels.Cars,
        on_delete=models.DO_NOTHING
    )
    idUser = models.ForeignKey(
        catalogModels.Users,
        on_delete=models.DO_NOTHING
    )

    class Meta:
        unique_together = ('idCar', 'idUser')
        db_table = 'AssignedCar'


class UsedCar(models.Model):
    expiration = models.DateTimeField()
    idAssignedCar = models.OneToOneField(
        AssignedCars,
        on_delete=models.DO_NOTHING,
        primary_key=True
    )

    class Meta:
        db_table = 'UsedCar'
