from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), min_length=2, max_length=12, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=20, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), min_length=8, max_length=20, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}), min_length=8, max_length=20, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2')



class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }