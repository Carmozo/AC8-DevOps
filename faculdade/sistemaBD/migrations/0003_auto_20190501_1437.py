# Generated by Django 3.0.dev20190427181822 on 2019-05-01 17:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaBD', '0002_auto_20190501_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='CPF',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999999999)], verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999999)], verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='CPF',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999999999)], verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='telefone',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999999)], verbose_name='Telefone'),
        ),
    ]
