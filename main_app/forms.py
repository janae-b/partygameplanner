from django.forms import ModelForm
from .models import Planning

class PlanningForm(ModelForm):
  class Meta:
    model = Planning
    fields = ['date', 'phase']