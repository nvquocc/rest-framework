from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from todo_list.models import Task
# Create your views here.


class TaskList(ListView):
    context_object_name = 'tasks'
    model = Task


class TaskDetail(DetailView):
    model = Task

    # return render(request, 'task/task_list.html', )
