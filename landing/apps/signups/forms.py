from django import forms
from .models import SignUp

class SignUpForms(forms.ModelForm):
	class Meta:
		model = SignUp