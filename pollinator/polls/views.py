from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Question, Choice
from .forms import QuestionForm
from django.urls import reverse

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

"""Original detail() method"""
"""
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})
"""

"""Making use of get_object_or_404() method"""
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})


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

def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Question(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )