from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from .forms import QuestionForm

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def mainPage(request):
	question_list = Question.objects.all()
	template = loader.get_template('polls/mainPage.html')
	context = {'question_list': question_list}
	return HttpResponse(template.render(context, request))

def get_question(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/main/')
		else:
			form = QuestionForm()
		return render(request, 'main.html', {'form': form})

