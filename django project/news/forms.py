from django import forms 
from news.models import News, NewsComments

class NewsAddForm(forms.ModelForm):
    class Meta:
        model = News
        fields = {'title', 'small_text','text','image', 'in_header','header_image',}
        
class NewsCommentsForm(forms.ModelForm):
    class Meta:
        model = NewsComments
        fields = {'text', }