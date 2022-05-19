from django.shortcuts import render





# Create your views here.
def book_view(request, ) :
    context ={}
    return render(request, 'book/book.html' ,context)

