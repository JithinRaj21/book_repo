from django.shortcuts import render

from .models import Books


# Create your views here.
def home(request):
    books = Books.objects.all()
    print(books)
    return render(request, 'home.html', {'books': books})
