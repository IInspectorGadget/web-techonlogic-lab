from django import forms 
from forum.models import ForumMessage, ForumMiddle


class ForumMessageForm(forms.ModelForm):
    class Meta:
        model = ForumMessage
        fields = {'message'}

class ForumMiddleForm(forms.ModelForm):
    class Meta:
        model = ForumMiddle
        fields = {'name'}


        

