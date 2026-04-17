from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPI(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer