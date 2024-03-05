from django import forms
from .models import Contatti

class ContattiForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        #link: https://www.youtube.com/watch?v=quJzUzCs6Q0

        # self.fields['nome'].widget.attrs['class']= 'form-control'
        # self.fields['email'].widget.attrs['class']= 'form-control'
        # self.fields['oggetto'].widget.attrs['class']= 'form-control'
        #Vado a dare la classe a tutti i fields visibili
        for vis in self.visible_fields():
            vis.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Contatti
        fields = '__all__'
