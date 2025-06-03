
from django import forms
#contact.html in form do name=name
class ContactForm(forms.Form):
    name=forms.CharField(label="name",max_length=30,required=True )
    email = forms.EmailField(label='email', max_length=100,required=True )
    message = forms.CharField(label='message',max_length=400,required=True )
