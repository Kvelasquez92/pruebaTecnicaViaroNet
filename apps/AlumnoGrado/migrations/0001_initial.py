# Generated by Django 2.1.5 on 2019-01-24 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Grado', '0001_initial'),
        ('Alumno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnoGrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(max_length=1)),
                ('alumnoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
                ('gradoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grado.Grado')),
            ],
        ),
    ]
