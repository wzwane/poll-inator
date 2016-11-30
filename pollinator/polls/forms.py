from django import forms

class QuestionForm(forms.Form):
	new_question = forms.CharField(label='New Question', max_length=100)