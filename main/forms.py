from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Imie'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nazwisko'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        help_texts = {
            'username':None,
        }



    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Login'  
        self.fields['password1'].widget.attrs['placeholder'] = 'hasło'  
        self.fields['password2'].widget.attrs['placeholder'] = 'powtórz hasło'   

        self.fields['email'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''

        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


