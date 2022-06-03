from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}), label=False)
	due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)

	class Meta:
		model = task
		fields = ['title', 'due']

class UpdateForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add task...'}))

	class Meta:
		model = task
		fields = ['title', 'due', 'complete']