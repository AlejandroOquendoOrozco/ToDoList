# Generated by Django 5.1 on 2024-08-24 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listatareas', '0005_delete_tarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=200)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
