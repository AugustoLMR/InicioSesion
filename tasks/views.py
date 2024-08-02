from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
from .forms import TaskCreationForm
#agregado
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import (
    CustomUserCreationForm,
    UserUpdateForm,
)
from django.contrib.auth import get_user_model
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from django.contrib.auth.views import (PasswordChangeView, PasswordChangeDoneView)

User = get_user_model()


def index(request):
    tasks = Task.objects.all()
    params = {
        'tasks': tasks,
    }
    return render(request, 'tasks/index.html', params)


def create(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        task = Task(title=title, content=content)
        task.save()
        return redirect('tasks:index')
    else:
        params = {
            'form': TaskCreationForm(),
        }
        return render(request, 'tasks/create.html', params)


def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    params = {
        'task': task,
    }
    return render(request, 'tasks/detail.html', params)


def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if (request.method == 'POST'):
        task.title = request.POST['title']
        task.content = request.POST['content']
        task.save()
        return redirect('tasks:detail', task_id)
    else:
        form = TaskCreationForm(initial={
            'title': task.title,
            'content': task.content,
        })
        params = {
            'task': task,
            'form': form,
        }
        return render(request, 'tasks/edit.html', params)


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if (request.method == 'POST'):
        task.delete()
        return redirect('tasks:index')
    else:
        params = {
            'task': task,
        }
        return render(request, 'tasks/delete.html', params)

class UserCreateAndLoginView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "tasks/signup.html"
    success_url = reverse_lazy("tasks:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=raw_pw)
        login(self.request, user)
        return response
    
class UserDetail(DetailView):
    model = User
    template_name = 'tasks/user_detail.html'
    
class UserUpdate(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'tasks/user_edit.html'

    def get_success_url(self):
        return reverse('tasks:user_detail', kwargs={'pk': self.kwargs['pk']})
    
class PasswordChange(PasswordChangeView):
    template_name = 'tasks/password_change.html'
    success_url = reverse_lazy('tasks:password_change_done')
    

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'tasks/user_detail.html'
    
class UserDelete(DeleteView):
    model = User
    template_name = 'tasks/user_delete.html'
    success_url = reverse_lazy('tasks:login')
    
