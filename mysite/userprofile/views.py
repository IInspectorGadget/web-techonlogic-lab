from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect , Http404
# from django.http import Http404
from django.urls import reverse
from django.db import connection
from django.views.generic import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.list import MultipleObjectMixin
from userprofile.models import  FriendRequest, User
from userprofile.forms import ProfileEditForm




class ProfileDetailView(DetailView):
    model = User
    template_name = 'profile/profile.html'
    slug_url_kwarg = 'username'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        profile = User.objects.get(slug = self.kwargs["username"])
        friends = profile.friends.all()[:5]
        context = super(ProfileDetailView, self).get_context_data(object_list=profile, friends=friends, **kwargs)
        return context
        

    def post(self, request, username):
        message = request.POST.get('message')
        user_id = request.user.id
        profile_id = request.POST.get('profile_id')
        return HttpResponse()


class ProfileFormView(UpdateView):
    model = User
    slug_url_kwarg = 'username'
    template_name = 'profile/profileForm.html'
    form_class = ProfileEditForm
    # def get_object(self):
    #     id = self.kwargs.get("id")
    #     return get_object_or_404(News, id=id)

    def dispatch(self, request, *args, **kwargs):        
        if(request.user.is_authenticated):
            if(request.user.slug != self.kwargs['username']):
                return redirect('main:index')
        else:
            return HttpResponseRedirect("%s?next=%s" % (reverse('accounts:login'),request.path))
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        username = self.kwargs['username']
        return reverse('profile:profile', kwargs={'username' : username.lower()})



def send_friend_request(request, username):
    if (request.user.is_authenticated == False):
        return HttpResponseRedirect("%s?next=%s" % (reverse('accounts:login'),request.path))

    profile = get_object_or_404(User, slug=username)
    check = profile.friends.filter(username = request.user.username)
    if (request.user.id != profile.id) and (not check):
        frequest, created = FriendRequest.objects.get_or_create(from_user=request.user,to_user=profile)
    return HttpResponseRedirect(reverse('profile:profile', kwargs= {'username' : username.lower()}))

def accept_friend_request(request, username):
    from_user = get_object_or_404(User, slug=username)
    frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    if frequest:
        user1 = frequest.to_user
        user2 = from_user
        user1.friends.add(user2.id)
        user2.friends.add(user1.id)
        frequest.delete()
    return HttpResponseRedirect(reverse('profile:profile', kwargs= {'username' : request.user.username.lower()}))



def deny_friend_request(request, username):
	from_user = get_object_or_404(User, slug=username)
	frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
	frequest.delete()
	return HttpResponseRedirect(reverse('profile:profile', kwargs= {'username' : request.user.username.lower()}))

def delete_friend_request(request, username, friend):
    if request.user.slug == username:
        user = get_object_or_404(User, slug=username)
        friend = user.friends.get(slug = friend)
        user.friends.remove(friend)
        friend.friends.remove(user)
    return HttpResponseRedirect(reverse('profile:profile', kwargs= {'username' : request.user.username.lower()}))


class SearchProfileView(ListView):
    model = User
    template_name = "profile/profileSearch.html"
    context_object_name='users'

    paginate_by = 20
   
    def get_queryset(self): 
        query = self.request.GET.get('username')
        if query:
            return User.objects.filter(username__icontains = query)
    
        return User.objects.all()



class ProfileFriendsView(DetailView, MultipleObjectMixin):
    model = User
    template_name = "profile/profileFriends.html"
    context_object_name='user'
    slug_url_kwarg = 'username'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('username')
        if query:
            object_list = User.objects.get(slug = self.kwargs.get('username')).friends.filter(username__icontains = query)
            context = super(ProfileFriendsView, self).get_context_data(object_list=object_list, **kwargs)
            return context
        object_list = User.objects.get(slug = self.kwargs.get('username')).friends.all()
        context = super(ProfileFriendsView, self).get_context_data(object_list=object_list, **kwargs)
        return context
    