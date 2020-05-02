from django import forms

class Signup(forms.Form):
    UserName=forms.CharField(label='UserName',max_length=100)
    Fname=forms.CharField(label='FirstName',max_length=20)
    Lname=forms.CharField(label='LastName',max_length=20,required=False)
    Email=forms.EmailField(label='Email',max_length=60,widget=forms.EmailInput)
    pic=forms.ImageField(label='Image')
    Password=forms.CharField(label='Password',max_length=100,widget=forms.PasswordInput)
class Login(forms.Form):
    UserName=forms.CharField(label='Username')
    Password=forms.CharField(label='Password',widget=forms.PasswordInput)