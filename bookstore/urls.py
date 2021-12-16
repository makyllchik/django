from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.list_object, name='book_view'),
    path("book/<int:id>/", views.detail, name="book_detail_view"),
]