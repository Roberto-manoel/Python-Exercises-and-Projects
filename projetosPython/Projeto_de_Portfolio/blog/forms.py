from django import forms
from .models import Comentario

class CommentForm(forms.ModelForm):
    conteudo = forms.CharField(widget=forms.Textarea(attrs={'autofocus': 'autofocus'}))

    class Meta:
        model = Comentario
        fields = ['conteudo']
