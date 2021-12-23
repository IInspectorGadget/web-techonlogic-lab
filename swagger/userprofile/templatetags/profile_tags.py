from django import template

register = template.Library()

# from django.shortcuts import get_object_or_404
from userprofile.models import FriendRequest, User


@register.simple_tag
def getFriendId(user, profile):
    try:
        bol = bool(user.friends.get(id = profile.id))
    except User.DoesNotExist:
        bol = False
    return bol 


@register.simple_tag
def checkRequest(user, profile):
    try:
        bol = bool(profile.to_user.get(from_user = user.id))
    except FriendRequest.DoesNotExist:
        bol = False
    return bol
