u'íóéáú'

from django import forms
from apps.Profesor.models import Profesor

class profesorForm(forms.ModelForm):
    class Meta:
        model = Profesor

        fields = '__all__'

        labels = {
            'nombre':'Nombre:',
            'apellidos':'Apellidos:',
            'genero':'Sexo:',
        }

        widgets = {
            'genero':forms.RadioSelect(choices=[('M','Masculino'),('F','Femenino')]),
        }
