# Generated by Django 5.0.3 on 2024-04-21 21:58

import cursos.models
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_estudiante_instructor_inscripcion_curso_estudiantes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='contenido',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AddField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(blank=True, default='cursos/fallback.png', upload_to='cursos'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='avatar',
            field=models.ImageField(blank=True, default='estudiante/fallback.png', upload_to='estudiante'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='avatar',
            field=models.ImageField(blank=True, default='instructor/fallback.png', upload_to='instructor'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='curso',
            name='precio',
            field=models.IntegerField(validators=[cursos.models.precio_positivo]),
        ),
    ]
