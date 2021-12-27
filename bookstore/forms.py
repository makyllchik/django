from django import forms
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            "title",
            "description",
            "image"
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = [
            'post',
            'text',
        ]
