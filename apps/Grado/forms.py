u'íóéáú'

from django import forms
from apps.Grado.models import Grado

class gradoForm(forms.ModelForm):
    class Meta:
        model = Grado

        fields = '__all__'

        labels = {
            'nombre':'Nombre:',
            'profesorId':'Profesor:',
        }

        widgets = {
            'nombre':forms.Select(choices=[('Kinder','Kinder'), ('Parvulos','Parvulos'), ('1ro Primaria','1ro Primaria'),
                                           ('2do Primaria','2do Primaria'), ('3ro Primaria','3ro Primaria'), ('4to Primaria','4to Primaria'),
                                           ('5to Primaria','5to Primaria'), ('6to Primaria','6to Primaria')]),
            'profesorId': forms.Select(),
        }
