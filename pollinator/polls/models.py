from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200, unique=True)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return 'Question: %s' % (self.question_text)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200, unique=True)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return 'Choice: %s' % (self.choice_text)

