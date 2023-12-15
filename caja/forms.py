from django.forms import ModelForm
from .models import Caja

class Caja(ModelForm):
    class Meta:
        model = Caja
        fields = []