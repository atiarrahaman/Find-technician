from django import forms 

from .models import User ,Profile
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm,UsernameField


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))



class SignupForm(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
    
    class Meta:
        model=User
        fields=['is_customer','is_mistri','username']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            
            
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name','bio','phone','email','description','profession','address']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'bio':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            
        }