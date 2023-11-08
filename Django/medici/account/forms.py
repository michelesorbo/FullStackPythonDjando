from django import forms
from django.contrib.auth.models import User
from .models import Profilo

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) #Creo un campo di tipo input type="password"

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Ripeti Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']

        #Controllo l'esattezza della seconda password
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Le password non coincidono')
            return cd['password2']
        
        #Verifico se la mail è già presente nel DB
        def clean_email(self):
            data = self.cleaned_data['email']
            if User.objects.filter(email=data).exists(): #Controllo se l'email inserita è già presente nel DB
                raise forms.ValidationError('Email già presente')
            return data
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

     #Verifico se la mail è già presente nel DB
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data) #Faccio la ricerca nel DB escludendo la mail corrente

        if qs.exists():
            raise forms.ValidationError('Email già presente')
        return data

class ProfiloEditForm(forms.ModelForm):
    class Meta:
        model = Profilo
        fields = ['data_nascita', 'img']