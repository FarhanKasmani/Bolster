from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
#User = get_user_model()
#from django.contrib.auth.forms import ReadOnlyPasswordHashField

class LoginForm(forms.Form):
    email = forms.EmailField(widget = forms.TextInput(attrs = {'class': "form-control",
        'type':"text",
        'name':"email",
        'placeholder':"Email"})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':"form-control",
        'type':"password",
        'name':"password",
        'placeholder':"Password"})
    )

class OtpForm(forms.Form):
    otp = forms.CharField(widget = forms.TextInput(attrs = {'class': "form-control",
        'type':"text",
        'name':"otp",
        'placeholder':"Enter OTP"})
    )
