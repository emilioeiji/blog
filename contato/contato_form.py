from django.forms import ModelForm
from contato.models import Contato


class FormContato(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'