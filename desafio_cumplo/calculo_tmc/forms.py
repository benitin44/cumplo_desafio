from django import forms

class CalculadoraForm(forms.Form):
    fecha = forms.DateField(widget=forms.DateInput)
    monto = forms.IntegerField(widget=forms.NumberInput)
    plazo = forms.IntegerField(widget=forms.NumberInput)
    is_reajustable = forms.BooleanField(widget=forms.CheckboxInput , required=False , initial=False)
    is_extranjera = forms.BooleanField(widget=forms.CheckboxInput , required=False, initial=False)
