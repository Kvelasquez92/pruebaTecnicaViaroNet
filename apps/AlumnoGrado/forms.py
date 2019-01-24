u'íóéáú'

from django import forms
from apps.AlumnoGrado.models import AlumnoGrado

class alumnoGradoForm(forms.ModelForm):
    class Meta:
        model = AlumnoGrado

        fields = '__all__'

        labels = {
            'alumnoId':'Asignar Alumno:',
            'gradoId':'Asignar Grado:',
            'seccion': 'Asignar Seccion',
        }

        widgets = {
            'alumnoId': forms.Select(),
            'gradoId': forms.Select(),
            'seccion': forms.Select(choices=[('U','Unica'),('A','A'),('B','B'),('C','C')]),
        }
