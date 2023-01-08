from django import forms
from django.forms import ModelForm
from .models import Report

class Reportform(ModelForm):
    class Meta:
        model = Report
        fields = ('location1','description','location2','security','cause','action','type_env','type_inju','type_property','type_vehicle')
        # widget = {'date':forms.DateInput( attrs= {'type': 'date'}), 'time':forms.TimeInput(attrs={'type':'time'})}