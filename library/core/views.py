from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'categories', 'description', 'published_year']
    template_name = 'book_form.html'
    success_url = reverse_lazy('profile')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'categories', 'description', 'published_year']
    template_name = 'book_form.html'
    success_url = reverse_lazy('profile')

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('profile')
from django.http import HttpResponse

def about(request):
    return HttpResponse("<h1>Бұл About беті</h1>")
def home_page(request):
    return HttpResponse("<h1>Басты бет</h1><p>Онлайн кітапханаға қош келдіңіз!</p>")
def user_by_id(request, user_id):
    return HttpResponse(f"Пайдаланушы ID: {user_id}")
def book_by_slug(request, slug):
    return HttpResponse(f"<h1>Кітапты іздеу</h1><p>Іздеу сөзі: {slug}</p>")
from django.urls import reverse
from django.http import HttpResponseRedirect

def go_to_profile(request):
    url = reverse('profile')
    return HttpResponseRedirect(url)
from django.shortcuts import redirect

def redirect_home(request):
    return redirect('home')
def numbers_only(request, numbers):
    return HttpResponse(f"<h1>Тек сандар қабылданды</h1><p>Сіз жіберген сандар: {numbers}</p>")