from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Question, Choice
from .forms import QuestionForm

def index(request):
	question_list = Question.objects.all()
	template = loader.get_template('polls/index.html')
	context = {
		'question_list': question_list,
	}
	return HttpResponse(template.render(context, request))


""" index() using render() method"""
"""
def index(request):
	question_list = Question.objects.all()
	context = {'question_list': question_list}
	return render(request, 'polls/index.html', context)
"""

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})

"""Just making use of get_object_or_404() method"""
"""
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
"""

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)

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