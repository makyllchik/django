from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


class BookListView(generic.ListView):
    template_name = 'list_object.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()


class BookDetailView(generic.DetailView):
    template_name = "detail.html"

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)


class BookCreateView(generic.CreateView):
    template_name = 'add_book.html'
    form_class = forms.BookForm
    success_url = '/books/'
    queryset = models.Book.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)


class BookUpdateView(generic.UpdateView):
    template_name = 'add_book.html'
    form_class = forms.BookForm

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)


class BookDeleteView(generic.DeleteView):
    template_name = 'book_delete.html'
    success_url = '/books/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)


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
