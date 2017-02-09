from django import forms

class SubmitJob(forms.Form):

    material_id = forms.CharField(max_length=8)
    workflow = forms.CharField(max_length=256)
    start_datepicker = forms.CharField(max_length=12)
    end_datepicker = forms.CharField(max_length=12)
