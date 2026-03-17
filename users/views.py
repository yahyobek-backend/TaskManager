from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages # Xabar ko'rsatish uchun

# Create your views here.


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_repeat = request.POST.get("password-repeat")

        # 1. Parollar mosligini tekshirish
        if password != password_repeat:
            messages.error(request, "Parollar bir-biriga mos kelmadi!")
            return redirect('register')

        # 2. Username bazada borligini tekshirish
        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu foydalanuvchi nomi band. Boshqa nom tanlang!")
            return redirect('register')

        # 3. Agar hammasi joyida bo'lsa, saqlash
        User.objects.create_user(username=username, password=password)
        messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
        return redirect('login')



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('login')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')

    return render(request, 'logout-confirmation.html')
