from django import forms

class InputForm(forms.Form):

    input = forms.CharField()

class ScatterPlotForm(forms.Form):
    
    polymer_1 = forms.BooleanField(initial=False, required=False)
    polymer_2 = forms.BooleanField(initial=False, required=False)
    polymer_3 = forms.BooleanField(initial=False, required=False)
    polymer_4 = forms.BooleanField(initial=False, required=False)
    carbon_high = forms.BooleanField(initial=False, required=False)
    carbon_low = forms.BooleanField(initial=False, required=False)
    silica_filler_1 = forms.BooleanField(initial=False, required=False)
    silica_filler_2 = forms.BooleanField(initial=False, required=False)
    plasticier_1 = forms.BooleanField(initial=False, required=False)
    plasticier_2 = forms.BooleanField(initial=False, required=False)
    plasticier_3 = forms.BooleanField(initial=False, required=False)
    antioxidant = forms.BooleanField(initial=False, required=False)
    coloring_pigment = forms.BooleanField(initial=False, required=False)
    Co_Agent_1 = forms.BooleanField(initial=False, required=False)
    Co_Agent_2 = forms.BooleanField(initial=False, required=False)
    Co_Agent_3 = forms.BooleanField(initial=False, required=False)
    Curing_Agent_1 = forms.BooleanField(initial=False, required=False)
    Curing_Agent_2 = forms.BooleanField(initial=False, required=False)
    Oven_temperature = forms.BooleanField(initial=False, required=False)
