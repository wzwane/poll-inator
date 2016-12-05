from django import forms
from models import Question, Choice

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['question_text']
		"""
		widgets = {
			'question_text': forms.TextInput(
				attrs={'id': 'question-text', 'required': True, 'placeholder': 'Ask a question'}
			),
		}
		"""

class ChoiceForm(forms.ModelForm):
	class Meta:
		model = Choice
		fields = ['choice_text']
