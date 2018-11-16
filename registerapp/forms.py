from django import forms
from .models import regmodel
class refrom(forms.ModelForm):
    class Meta:
        model = regmodel
        fields=['fname','lname','email','username','password','contact','gender']

    fname=forms.CharField(
        label="First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter the First Name'
            }
        )
    )
    lname=forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter the Last name'
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter the email'
            }
        )
    )
    username=forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter the Username'
            }
        )
    )
    password=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter the password'
            }
        )
    )
    contact=forms.IntegerField(
        label='Mobile No.',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter the contact no.'
            }
        )
    )
    gender = forms.ChoiceField(
        choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    )
class loginform(forms.Form):
    username=forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter the Username'
            }
        )
    )
    password=forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter The Password'
            }
        )
    )