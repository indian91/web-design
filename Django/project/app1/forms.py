from django import forms

class Signup(forms.Form):
    UserName=forms.CharField(label='Username',max_length=50)
    Fname=forms.CharField(label='Fname',max_length=50)
    Lname=forms.CharField(label='Lname',max_length=50)
    Email=forms.EmailField(label='Email')
    Password=forms.CharField(label='Password',widget=forms.PasswordInput)
class Login(forms.Form):
        UserName=forms.CharField(label='Username',max_length=50)
        Password=forms.CharField(label='Password',widget=forms.PasswordInput)
