from django import forms
from . models import Todo


class ToForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ['title']