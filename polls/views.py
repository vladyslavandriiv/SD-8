from django.shortcuts import render

from django.shortcuts import render
from .models import Question

def question_list(request):
    questions = Question.objects.all().order_by('-pub_date')
    return render(request, 'polls/question_list.html', {'questions': questions})