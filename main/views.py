from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views import View
# Create your views here.

class HomeView(View):

    def get(self, request):
        tasks = Task.objects.all()

        context = {
            'tasks': tasks,
        }
        return render(request, 'index.html', context)

    def post(self, request):
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            status=request.POST['status'],
            deadline=request.POST.get('deadline') if request.POST.get('deadline') else None
        )
        return self.get(request)

class EditTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)

        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.status = request.POST['status']
        task.save()
        return redirect('home')

class DeleteConfirmTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)

        context = {
            'task': task,
        }
        return render(request, 'task-confirmation.html', context)

class DeleteTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('home')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')