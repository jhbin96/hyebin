from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm): #ModelForm import
    class Meta:
        model = Article #Article import
        fields = ['title', 'image', 'content']
