from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import Book, Author

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

# 1-тапсырма: hello
def hello(request):
    return HttpResponse("Сәлем, Django!")
# about беті
def about(request):
    return HttpResponse("<h1>Бұл About беті</h1>")

# home_page
def home_page(request):
    return HttpResponse("<h1>Басты бет</h1><p>Онлайн кітапханаға қош келдіңіз!</p>")

# user_by_id
def user_by_id(request, user_id):
    return HttpResponse(f"Пайдаланушы ID: {user_id}")

# book_by_slug
def book_by_slug(request, slug):
    return HttpResponse(f"<h1>Кітапты іздеу</h1><p>Іздеу сөзі: {slug}</p>")

# go_to_profile
def go_to_profile(request):
    from django.urls import reverse
    from django.http import HttpResponseRedirect
    url = reverse('profile')
    return HttpResponseRedirect(url)

# redirect_home
def redirect_home(request):
    from django.shortcuts import redirect
    return redirect('home')

# numbers_only
def numbers_only(request, numbers):
    return HttpResponse(f"<h1>Тек сандар қабылданды</h1><p>Сіз жіберген сандар: {numbers}</p>")

# 2-тапсырма: index_view
def index_view(request):
    context = {'name': 'Zhanel'}
    return render(request, 'index.html', context)

# 3-тапсырма: feedback_view
def feedback_view(request):
    message = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = f"Рақмет, {name}! Сіздің хатыңыз қабылданды."
    return render(request, 'feedback.html', {'message': message})

# 4-тапсырма: redirect
def feedback_redirect_view(request):
    if request.method == 'POST':
        return redirect('thank_you')
    return render(request, 'feedback.html')

def thank_you_view(request):
    return HttpResponse("Рақмет! Форма сәтті жіберілді.")

# 5-тапсырма: JSON status
def status_view(request):
    return JsonResponse({'status': 'ok', 'message': 'Сервер жұмыс істейді'})

# 6-тапсырма: TemplateView
class AboutPageView(TemplateView):
    template_name = 'about_page.html'

# 7-тапсырма: ListView
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

# 8-тапсырма: DetailView
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

# 9-тапсырма: CreateView (Author)
class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'bio']
    template_name = 'author_form.html'
    success_url = reverse_lazy('book_list')

# 10-тапсырма: DeleteView (Author)
class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('book_list')