from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
   name=forms.CharField(label='',max_length=30,required=True,widget=forms.TextInput(attrs={'class':'form_control my-2','placeholder':'Enter you name'}))
   email=forms.EmailField(label='',max_length=40,required=True,widget=forms.EmailInput(attrs={'class':'form_control my-2','placeholder':'Enter you email'}))
   message=forms.CharField(label='',max_length=400,required=True,widget=forms.Textarea(attrs={'class':'form_control my-2','placeholder':'Feedback'}))

   def clean(self):
       if self.errors:
           return self.cleaned_data
       cleaned_data = super().clean()

       valid_name=cleaned_data['name']
       if len(valid_name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
       
class StudentForm(forms.ModelForm):
    name=forms.CharField(label='',max_length=30,required=False,widget=forms.TextInput(attrs={'class':'form_control my-2','placeholder':'Enter you name'}))
    age=forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':'form_control my-2','placeholder':'Enter your age'}))

    class Meta :
      model = Student
      fields= '__all__'

class RegisterForm(forms.ModelForm):
   username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter your name'}))
   email = forms.EmailField(max_length=40, required=True, widget=forms.EmailInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter your email'}))
   password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter password'}))
   confirm_password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Confirm password'}))

   def clean(self):
        
        if self.errors:
            return self.cleaned_data


        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.") 
        return cleaned_data 

   class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter your name'}))
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter password'}))
        # password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter password',type:'password'}))

       
       
       


