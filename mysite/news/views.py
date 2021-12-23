import json
# Create your views here.
# from django.contrib.auth.hashers import make_password
# from django.http import HttpResponseRedirect , Http404
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
# from django.shortcuts import get_object_or_404

from django.views.generic import DetailView
from django.views.generic.edit import FormView, UpdateView, CreateView
# from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
# from django.views.generic.detail import BaseDetailView
from django.http import HttpResponse
# from django.http import JsonResponse
# from django.forms.models import model_to_dict
# from django.core.serializers import get_serializer
from django.views.generic.base import View

from django.views.generic.list import MultipleObjectMixin


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db.models import Q
from news.forms import NewsAddForm, NewsCommentsForm
from news.models import LikeDislike, News, NewsComments
from userprofile.models import User
from django.contrib.contenttypes.models import ContentType

#отображение списка новостей
class NewsListView(ListView):
    model = News
    template_name = 'news/news.html'
    context_object_name = 'news'

    paginate_by = 15

#отображение новости + добавление коментариев 
class NewsDetailView(FormView, DetailView, MultipleObjectMixin):
    model = News
    template_name = "news/newsDetail.html"
    pk_url_kwarg = 'id'
    context_object_name = 'new'

    paginate_by = 15

    form_class = NewsCommentsForm

    def get_context_data(self, **kwargs):
        object_list = NewsComments.objects.filter(news=self.get_object())
        context = super(NewsDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.news = News.objects.get(id=self.kwargs.get('id'))
        comment.author = User.objects.get(id=self.request.user.id)
        comment.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return "%s?page=%s" % (reverse('news:newsDetail', args=[self.kwargs.get('id')]), self.request.GET.get("page"))

#создание новости
class NewsFormView(PermissionRequiredMixin, CreateView):
    model = News
    form_class = NewsAddForm
    template_name = 'news/newsAdd.html'

    permission_required = "news.add_news"


    def form_valid(self, form):
        news = form.save(commit=False)
        if(self.request.user.is_authenticated):
            news.author = self.request.user
            news.save()
        # News.objects.create(**form.cleaned_data)
        return redirect(self.get_success_url())
    def get_success_url(self):
        return reverse('news:news')

#редактирование новости
class NewsEditView(PermissionRequiredMixin ,UpdateView):
    model = News
    form_class = NewsAddForm
    template_name = 'news/newsEdit.html'
    pk_url_kwarg = 'id'

    permission_required = "news.change_news"


    # permission_denied_message = 'dsadsadsadsa'
    def form_valid(self, form):
        news = form.save(commit=False)
        news.save()
        return redirect(self.get_success_url())
    def get_success_url(self):
        return reverse('news:news')




class VotesView(View):
    model = None    # Модель данных - Статьи или Комментарии
    vote_type = None # Тип комментария Like/Dislike
    
    def post(self, request, pk):
        # берём нужную модель
        obj = self.model.objects.get(pk=pk)
        # print(ContentType.objects.get_for_model(obj))
        # GenericForeignKey не поддерживает метод get_or_create
        try:
            # print(self.vote_type)
            #получаем модель у которой content_type news с id и id (шобы изменить данные)
            likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id, user=request.user)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True
 
        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.votes.likes().count(),
                "dislike_count": obj.votes.dislikes().count(),
                "sum_rating": obj.votes.sum_rating()
            }),
            content_type="application/json"
        )





    