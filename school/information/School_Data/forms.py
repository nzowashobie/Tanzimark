from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import Users

from School_Data.models import Students

class ImageForm(forms.ModelForm):
        """Form for the image model"""
        class Meta:
            model = Students
            fields = ('name','Subject', 'IMAGES','Grade')
			
widgets = {
            	'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            	'Subject': forms.Textarea(attrs={'class': 'form-control','placeholder': 'subject'}),
				'Grade': forms.Textarea(attrs={'class': 'form-control','placeholder': 'grade'}),
        }


#search form

class NewUserForm(UserCreationForm):
	Phone_no = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ("username", "Phone_no", "password1", "password2")
	
class AddressForm(forms.Form):
  
    
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.Phone_no = self.cleaned_data['Phone_no']
		if commit:
			user.save()
		return user


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user