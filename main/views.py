from django.shortcuts import render
from news.models import News
from forum.models import ForumMiddle
from django.views.generic.base import View

class IndexView(View):
    def get(self, request):
        head_list = News.objects.filter(in_header=True)
        news_list = News.objects.filter(in_header=False)[:6]

        forum = ForumMiddle.objects.all().order_by('-post_count')[:10]

        context = {'news_list': news_list,'head_list' : head_list, 'forumMiddle' : forum}
        return render(request,'index.html', context)

class InfoView(View):
    def get(self, request):
        return render(request, 'info.html', {})
    