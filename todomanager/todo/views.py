from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from todo.models import Task
from todo.forms import TaskCreateForm


class TaskListView(ListView):
    """Documentation de notre controleur."""
    model = Task
    context_object_name = "tasks"
    template_name = "todo/tasks-list.html"
    paginate_by = None

class TaskRetrieveView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "todo/task-details.html"

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "todo/task-create.html"

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "todo/task-create.html"

class TaskDelete(DeleteView):
    model = Task
    template_name = "todo/task-delete.html"
    

    # def get_initial(self):
    #     return {'created_by': self.request.user.member,
    #             'modified_by': self.request.user.member,
    #             'assigned_to': self.request.user.member}				