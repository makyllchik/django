from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book_view'),
    path("books/<int:id>/", views.BookDetailView.as_view(), name="book_detail_view"),
    path('add-book/', views.BookCreateView.as_view(), name='add_book_view'),
    path("books/<int:id>/update/", views.BookUpdateView.as_view(), name="book_update_view"),
    path("books/<int:id>/delete/", views.BookDeleteView.as_view(), name="book_delete_view"),
    path('add-comment/', views.add_comment, name='add_comment_view'),
]
