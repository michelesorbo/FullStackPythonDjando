from django import forms

class CouponApplicaForm(forms.Form):
    codice = forms.CharField()