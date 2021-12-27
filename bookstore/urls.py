from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_object, name='book_view'),
    path("books/<int:id>/", views.detail, name="book_detail_view"),
    path('add-book/', views.add_book, name='add_book_view'),
    path('add-comment/', views.add_comment, name='add_comment_view'),
]
