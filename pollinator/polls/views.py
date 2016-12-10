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
	form = ChoiceForm();
	context = {
		'question': question,
		'form': form,
	}
	return render(request, 'polls/detail.html', context)

# def results(request, question_id):
# 	response = "You're looking at the results of question %s."
# 	return HttpResponse(response % question_id)

"""Creates a question and updates the database"""
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
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/jsons"
		)

"""Creates a choice and updates the database"""
def create_choice(request, question_id):
	if request.method == 'POST':
		choice_text = request.POST.get("the_choice")
		response_data = {}

		question = Question.objects.get(pk=question_id)
		"""Below will be uncommented later to actually save the choice in DB"""
		choice = question.choice_set.create(choice_text=choice_text)

		response_data['result'] = 'Create choice successful'
		response_data['questionpk'] = question.pk
		response_data['question_text'] = question.question_text
		response_data['choicepk'] = choice.pk
		response_data['choice_votes'] = choice.votes
		response_data['choice_text'] = choice_text

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/jsons"
		)

"""Updates the votes field of a choice instance"""
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['the_selected'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		response_data = {}
		response_data['choicepk'] = selected_choice.pk
		response_data['choice_votes'] = selected_choice.votes
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)