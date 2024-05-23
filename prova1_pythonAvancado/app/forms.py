from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import *
from .models import *




class FormImagem(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ["titulo","imagem"]
        labels = {"titulo": "", "imagem": ""}
        widgets = {"imagem":URLInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update(
            {'placeholder':"Titulo da Imagem", 'class': 'form-control my-2 p-2'})
        self.fields['imagem'].widget.attrs.update(
            {'placeholder':"Link da Imagem",'class': 'form-control my-2 p-2'})
        

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','password','first_name','last_name','email']
        widgets = {'password': PasswordInput(),'email':EmailInput()}
    def __init__ (self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['username'].widget.attrs.update({'required':'True','placeholder':'Login','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['password'].widget.attrs.update({'required':'True','placeholder':'Senha','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['first_name'].widget.attrs.update({'required':'True','placeholder':'Prenome','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['last_name'].widget.attrs.update({'required':'True','placeholder':'Sobrenome','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['email'].widget.attrs.update({'required':'True','placeholder':'Email','class':'col form-control my-2 p-2','autocomplete':'new-password'})

