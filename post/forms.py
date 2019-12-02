from django import forms
from .models import Posts,comment


class FormPost(forms.ModelForm):

    class Meta:
        model=Posts
        fields= [

            'title',
            'content',
            'image',
        ]


class CommentForm(forms.ModelForm):

    class Meta:
        model=comment
        fields=(
            'name',
            'content',
        )