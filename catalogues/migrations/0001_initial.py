# Generated by Django 2.2.3 on 2019-07-24 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('username', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
