from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from .views import (
    register, CustomLoginView, profile, BookCreateView,
    BookUpdateView, BookDeleteView, about, home_page,
    user_by_id, book_by_slug, go_to_profile, redirect_home,
    numbers_only, hello, index_view, feedback_view, status_view,
    BookListView, BookDetailView, AuthorCreateView, AuthorDeleteView, AboutPageView
)
from .views_api import BookListAPI, BookDetailAPI

urlpatterns = [
    path('', home_page, name='home'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile, name='profile'),
    path('about/', about, name='about'),
    path('books/add/', BookCreateView.as_view(), name='add_book'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='edit_book'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='delete_book'),
    path('user/<int:user_id>/', user_by_id, name='user_by_id'),
    path('book/<slug:slug>/', book_by_slug, name='book_by_slug'),
    path('go-profile/', go_to_profile, name='go_to_profile'),
    path('home/', redirect_home, name='redirect_home'),
    re_path(r'^numbers/(?P<numbers>\d+)/$', numbers_only, name='numbers_only'),
    path('api/books/', BookListAPI.as_view(), name='api_book_list'),
    path('api/books/<int:pk>/', BookDetailAPI.as_view(), name='api_book_detail'),
    
    # 4-лаб (Views) тапсырмалары
    path('hello/', hello, name='hello'),
    path('index/', index_view, name='index'),
    path('feedback/', feedback_view, name='feedback'),
    path('status/', status_view, name='status'),
    path('about-page/', AboutPageView.as_view(), name='about_page'),
    path('books-list/', BookListView.as_view(), name='book_list'),
    path('book-detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('author-add/', AuthorCreateView.as_view(), name='author_add'),
    path('author-delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),
]