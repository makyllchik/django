from django.http import Http404
from django.shortcuts import render
from . import models


def list_object(request):
    post = models.Book.objects.all()
    return render(request, 'post_list.html', {'post': post})


def detail(request, id):
    try:
        post = models.Book.objects.get(id=id)
    except models.Book.DoesNotExist:
        raise Http404("Post does not Exist")

    return render(request, "post_detail.html", {"post": post})