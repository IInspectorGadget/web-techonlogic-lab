from django import template
register = template.Library()

from news.models import LikeDislike
from django.contrib.contenttypes.models import ContentType

@register.simple_tag
def checkUserLike(new, user):
    try:
        l = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(new), object_id=new.id, user=user)
    except:
        return False
    
    if l.vote == 1:
        return 'green'
    else: 
        return 'red'