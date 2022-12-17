from django import forms 

from .models import User ,Profile ,CustomerRating
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm,UsernameField


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))



class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','is_mistri','is_tutor','is_customer']
       



class ProfileForm(forms.ModelForm):
    aggre=forms.BooleanField(required=True)
    class Meta:
        model=Profile
        fields=['name','bio','phone','email','description','skill','add_more_skill','address','profile_pic','aggre']
       
            
            
class ProfileFormTutor(forms.ModelForm):
    tutor=forms.BooleanField(required=True)
    class Meta:
        model=Profile
        fields=['name','bio','phone','email','description','clases','add_more_clases','subjects','add_more_subject','address','profile_pic','tutor']    

class ReviewForm(forms.ModelForm):
    class Meta:
        model=CustomerRating
        fields=['rating','review']