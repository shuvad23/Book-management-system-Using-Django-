from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Book
from .forms import BookForm,EditBookForm
# Create your views here.

def homepage(request):
    books= Book.objects.all()
    context={
        'books':books
    }
    return render(request,'book_list.html',context)


def add_book(request):
    if request.method == 'POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book added Successfully!')
            return redirect('/')
    else:
        form=BookForm() 
        context={
            'form':form
        }
        return render(request,'add_book.html',context)

def edit_book(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    if request.method =='POST':
        form=EditBookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            messages.success(request,'Book updated Successfully!')
            return redirect('/')
    else:
        form=EditBookForm(instance=book)
        context={
            'form':form
        }
        return render(request,'add_book.html',context)
    
    


def delete_book(request,book_id):
    book=Book.objects.get(id=book_id)
    book.delete()
    messages.success(request,'Book deleted Successfully!')
    return redirect('/')