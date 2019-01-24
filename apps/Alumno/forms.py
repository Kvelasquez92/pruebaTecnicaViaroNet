u'íóéáú'

from django import forms
from datetime import datetime
from apps.Alumno.models import Alumno

class alumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno

        fields = '__all__'

        labels = {
            'nombre':'Nombre:',
            'apellidos':'Apellidos:',
            'genero':'Sexo:',
            'fechaNacimiento':'Fecha de Nacimiento:',
        }

        widgets = {
            'genero':forms.RadioSelect(choices=[('M','Masculino'),('F','Femenino')]),
            'fechaNacimiento':forms.SelectDateWidget(years=range(datetime.today().year-25, datetime.today().year - 4))
        }
