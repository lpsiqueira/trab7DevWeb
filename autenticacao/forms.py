from django import forms

class Login(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-group'})
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-group'})
    )