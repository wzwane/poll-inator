from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Choice

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def mainPage(request):
	question_list = Question.objects.all()
	template = loader.get_template('polls/mainPage.html')
	context = {'question_list': question_list}
	return HttpResponse(template.render(context, request))