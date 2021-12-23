from django import forms 
from news.models import News, NewsComments

#форма создания/редактирования новости
class NewsAddForm(forms.ModelForm):
    class Meta:
        model = News
        fields = {'title', 'small_text','text','image', 'in_header','header_image',}

#форма для создание коментариев     
class NewsCommentsForm(forms.ModelForm):
    class Meta:
        model = NewsComments
        fields = {'text', }