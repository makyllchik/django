from django.http import Http404, HttpResponse
from django.shortcuts import render
from . import models, forms


def list_object(request):
    book = models.Book.objects.all()
    return render(request, 'list_object.html', {'book': book})


def detail(request, id):
    try:
        book = models.Book.objects.get(id=id)
        try:
            comment = models.Comment.objects.filter(post_id=id).order_by("created_date")
        except models.Comment.DoesNotExist:
            return HttpResponse("No comments")

    except models.Book.DoesNotExist:
        raise Http404("Book does not Exist, fool")

    return render(request, "detail.html", {"book": book, "book_comment": comment})


def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        print(form.data)
        models.Book.objects.create(title=form.data["title"],
                                   description=form.data["description"],
                                   image=form.data["image"])
        return HttpResponse("Book created successfully")
    else:
        form = forms.BookForm()

    return render(request, "add_book.html", {"form": form})


def add_comment(request):
    method = request.method
    if method == "POST":
        form = forms.CommentForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponse('Comment created Successfully')
    else:
        form = forms.CommentForm()
    return render(request, 'add_comment.html', {'form': form})
