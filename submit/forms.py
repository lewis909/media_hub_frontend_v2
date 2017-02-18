from django import forms
from asset_db.models import Profiles, AssetMetadata


class SubmitJob(forms.Form):

    material_id = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'class': 'autocomplete'}))
    workflow = forms.ModelChoiceField(queryset=Profiles.objects.distinct('name'), to_field_name='name')
    start_datepicker = forms.CharField(max_length=12, widget=forms.DateInput(attrs={'class': 'datepicker'}))
    end_datepicker = forms.CharField(max_length=12, widget=forms.DateInput(attrs={'class': 'datepicker'}))

