from django.forms import ModelForm
from .models import Party

class PartyForm(ModelForm):
  class Meta:
    model = Party
    fields = ['date', 'phase']