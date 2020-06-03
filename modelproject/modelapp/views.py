from django.shortcuts import render
from .models import Article

# Create your views here.
# 데이터를 가공 처리해야 할때 사용

def home(request):
    article = Article.objects
    return render(request,'home.html',{'article':article})