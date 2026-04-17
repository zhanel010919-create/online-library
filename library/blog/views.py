from django.shortcuts import render
from django.http import HttpResponse

def blog_list(request):
    return HttpResponse("<h1>Блог тізімі</h1><p>Барлық посттар осында</p>")

def blog_detail(request, pk):
    return HttpResponse(f"<h1>Блог пост №{pk}</h1><p>Посттың мазмұны</p>")