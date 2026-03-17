from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        tasks = Task.objects.filter(user=request.user)

        status_filter = request.GET.get('status')

    # Agar status_filter bo'sh bo'lsa (ya'ni "Hammasi" tanlansa),
    # bu blok ishlamaydi va hamma tasklar qaytadi
        if status_filter:
            tasks = tasks.filter(status=status_filter)

    # Doim eng yangi tasklar tepada turishi uchun tartiblaymiz
        tasks = tasks.order_by('-created_at')

        context = {'tasks': tasks}
        return render(request, 'index.html', context)

    def post(self, request):
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            status=request.POST['status'],
            deadline=request.POST.get('deadline') if request.POST.get('deadline') else None,
            user=request.user,
        )
        return self.get(request)

class EditTaskView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)

        context = {
            'task': task,
        }
        return render(request, 'edit.html', context)

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.status = request.POST['status']
        task.save()
        return redirect('home')

class DeleteConfirmTaskView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)

        context = {
            'task': task,
        }
        return render(request, 'task-confirmation.html', context)

class DeleteTaskView(LoginRequiredMixin,View):
    login_url = 'login'
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.delete()
        return redirect('home')


