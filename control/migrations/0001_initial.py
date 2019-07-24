# Generated by Django 2.2.3 on 2019-07-24 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedCars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalogues.Cars')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalogues.Users')),
            ],
            options={
                'db_table': 'AssignedCar',
                'unique_together': {('idCar', 'idUser')},
            },
        ),
        migrations.CreateModel(
            name='UsedCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration', models.DateTimeField()),
                ('idAssignedCar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='control.AssignedCars', unique=True)),
            ],
            options={
                'db_table': 'UsedCar',
            },
        ),
    ]