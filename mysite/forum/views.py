from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.views.generic.list import ListView, MultipleObjectMixin
from forum.forms import ForumMessageForm, ForumMiddleForm
from forum.models import ForumMessage, ForumMiddle, ForumTitle, ForumTop

#отображение разделов форума
class ForumTitleView(ListView):
    model = ForumTitle
    template_name = 'forum/forumTitle.html'
    context_object_name = 'forumTitles'

#отображение тем форума + создание темы
class ForumTopView(FormView, DetailView, MultipleObjectMixin):
    model = ForumTop
    template_name = "forum/forumTop.html"
    pk_url_kwarg = 'id'
    context_object_name = 'forumTop'
    paginate_by = 10

    form2 = ForumMessageForm()

    form_class = ForumMiddleForm
    def form_valid(self, form):

        forumMiddle = form.save(commit=False)
        forumMiddle.forumTop = ForumTop.objects.get(id=self.kwargs.get('id'))
        forumMiddle.user_id = self.request.user.id 

        message = self.request.POST.get('message')
        forumMessage = ForumMessage()
        forumMessage.message = message
        forumMessage.user_id = self.request.user.id 

        forumMiddle.save()
        forumMessage.forumMiddle = forumMiddle
        forumMessage.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
        return "%s?page=%s" % (reverse('forum:forumTop', args=[self.kwargs.get('id')]), self.request.GET.get("page"))

    def get_context_data(self, **kwargs):
        object_list = ForumMiddle.objects.filter(forumTop=self.get_object()).order_by('-post_count')
        context = super(ForumTopView, self).get_context_data(object_list=object_list, form2=self.form2, **kwargs)
        return context

#отображение под-тем форума + создание коментариев
class ForumMiddleView(FormView, DetailView, MultipleObjectMixin):
    model = ForumMiddle
    template_name = "forum/forumMiddle.html"
    pk_url_kwarg = 'middle_id'
    context_object_name='forumMiddle'
    form_class = ForumMessageForm

    paginate_by = 10


    def form_valid(self, form):
        message = form.save(commit=False)
        middle_id = self.kwargs.get('middle_id')
        message.forumMiddle = ForumMiddle.objects.get(id=middle_id)
        message.user_id = self.request.user.id
        message.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return "%s?page=%s" % (reverse('forum:forumMiddle', args=[self.kwargs.get('id'), self.kwargs.get('middle_id')]), self.request.GET.get("page"))

    def get_context_data(self, **kwargs):
        object_list = ForumMessage.objects.filter(forumMiddle=self.get_object())
        context = super(ForumMiddleView, self).get_context_data(object_list=object_list, **kwargs)
        return context