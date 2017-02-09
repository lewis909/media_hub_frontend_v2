from django import forms
from asset_db.models import Profiles
class SubmitJob(forms.Form):


    material_id = forms.CharField(max_length=8)
    workflow = forms.ModelChoiceField(queryset=Profiles.objects)
    start_datepicker = forms.CharField(max_length=12)
    end_datepicker = forms.CharField(max_length=12)
