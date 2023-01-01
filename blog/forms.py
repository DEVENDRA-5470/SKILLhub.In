from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UsernameField,AuthenticationForm,SetPasswordForm


# signup form-----------------------------------------------------------------------------------
class SignForm(UserCreationForm):
    password1=forms.CharField(
        label=('Password'),
        widget=forms.PasswordInput(attrs={'placeholder':'Password',
        'class':'rounded'
        })
    )
    
    password2=forms.CharField(
        label=("Confirm Password"),
        widget=forms.PasswordInput(attrs={"placeholder":'Re-password',
        'class':'rounded'
        })
    )
    class Meta:
        model=User
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter username',
            'class':'rounded'}),
            'email':forms.TextInput(attrs={'placeholder':'Email address',
            'class':'rounded'})
        }


# loginform----------------------------------------------------------------------------------------
class Login_form(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={"placeholder":"Username",'class':'rounded-full focus:bg-red-200 '}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'rounded-full focus:bg-red-200'}))


# set password-----------------------------------------------------------------------------------------

class Set_password(SetPasswordForm):
    new_password1=forms.CharField(
        label=('New Password'),
        widget=forms.PasswordInput(attrs={'placeholder':'New Password','class':'rounded-full focus:bg-red-200 '})
    )
    new_password2=forms.CharField(
        label=('Confirm Password'),
        widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'rounded-full focus:bg-red-200 '})
    )
