from ..models import Curso, Instructor, Categoria
from django import forms


class CursoForm(forms.ModelForm):

    instructor = forms.ModelChoiceField(
        queryset=Instructor.objects.all(),
        required=False,
        empty_label="Selecciona un instructor",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        empty_label="Selecciona una categoría",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Curso
        fields = [
            "nombre",
            "descripcion",
            "precio",
            "fecha_publicacion",
            "instructor",
            "categoria",
            "duracion",
            "estado",
            "destacado",
        ]
        labels = {
            "nombre": "Nombre del curso",
            "descripcion": "Descripción",
            "precio": "Precio",
            "fecha_publicacion": "Fecha de publicación",
            "instructor": "Instructor",
            "categoria": "Categoría",
            "duracion": "Duración",
            "estado": "Estado",
            "destacado": "Destacado",
        }

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del curso"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descripción del curso"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Precio del curso"}),
            "fecha_publicacion": forms.NumberInput(attrs={"class": "form-control", "type": "date", "placeholder": "Ingrese la fecha"}),
            "duracion": forms.TimeInput(attrs={"class": "form-control", "placeholder": "Duración del curso"}),
            "estado": forms.Select(attrs={"class": "form-control"}),
            "destacado": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }