from books.models import Book
from django.shortcuts import render, redirect


# from project.books.models import Book


def add_book(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']

        books = Book.objects.create(name=name, author=author, isbn=isbn, category=category)
        books.save()
        alert = True
        return render(request, "user/add_book.html", {'alert': alert})
    return render(request, "user/add_book.html")


def view_books(request):
    books = Book.objects.all()
    return render(request, "user/allbooks.html", {'books': books})


def delete_book(request, myid):
    books = Book.objects.filter(id=myid)
    books.delete()
    return redirect("/allbooks")


def update(request):
    pass
