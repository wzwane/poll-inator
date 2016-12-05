from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader, RequestContext

from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm
from django.urls import reverse

import json

"""Renders the main page (index.html)"""
def index(request):
	question_list = Question.objects.all()  # fetch the list of questions from DB
	form = QuestionForm();
	context = {
		'question_list': question_list,
		'form': form,
	}
	return render(request, 'polls/index.html', context)

"""Renders the question page (detail.html)"""
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	form = ChoiceForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("choice_text")
		instance.save()
	context = {
		'question': question,
		'form': form,
	}
	return render(request, 'polls/detail.html', context)

# def question_update(request, id=None):
# 	instance = get_object_or_404(Question, id=id)
# 	form = QuestionForm(request.POST or None, instance=instance)  # get input from the form
# 	if form.is_valid():  # if fields are validated
# 		instance = form.save(commit=False)
# 		instance.save()
# 		return HttpResponseRedirect(instance.get_absolute_url())
# 	context = {
# 		'question_text': instance.question_text,
# 		'instance': instance,
# 		'form': form,
# 	}
# 	return render(request, "question_form.html", context)






def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('results', args=(question.id,)))

# def get_question(request):
# 	if request.method == 'POST':
# 		form = QuestionForm(request.POST)
# 		if form.is_valid():
# 			return HttpResponseRedirect('/main/')
# 		else:
# 			form = QuestionForm()
# 		return render(request, 'main.html', {'form': form})

def create_question(request):
	if request.method == 'POST':
		question_text = request.POST.get("the_question")
		response_data = {}

		question = Question(question_text=question_text)
		question.save()

		response_data['result'] = 'Create question successful'
		response_data['questionpk'] = question.pk
		response_data['question_text'] = question.question_text

		return HttpResponse(
			json.dumps(response_data),
			contet_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/jsons"
		)