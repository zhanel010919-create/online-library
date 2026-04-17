from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')
    categories_list = serializers.StringRelatedField(many=True, source='categories')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'categories_list', 'description', 'published_year']