from django import forms 
from forum.models import ForumMessage, ForumMiddle

#форма для создания сообщения
class ForumMessageForm(forms.ModelForm):
    class Meta:
        model = ForumMessage
        fields = {'message'}

#форма для создания под-темы
class ForumMiddleForm(forms.ModelForm):
    class Meta:
        model = ForumMiddle
        fields = {'name'}


        

