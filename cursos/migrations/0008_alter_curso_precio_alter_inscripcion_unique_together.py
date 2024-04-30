# Generated by Django 5.0.3 on 2024-03-27 20:11

import cursos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cursos", "0007_estudiante_instructor_inscripcion_curso_estudiantes_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="precio",
            field=models.IntegerField(validators=[cursos.models.precio_positivo]),
        ),
        migrations.AlterUniqueTogether(
            name="inscripcion",
            unique_together={("estudiante", "curso")},
        ),
    ]