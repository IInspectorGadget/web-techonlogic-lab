from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from news.models import News
from forum.models import ForumMiddle
from django.views.generic.base import View
from userprofile.models import User, Telegram
from django.contrib.auth.hashers import check_password

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
    

def telegramPassword(request):
    if request.method == "GET":
        users = User.objects.filter(username=request.GET['username'])
        if len(users) == 1:
            user = users[0]
            if user.check_password(request.GET['password']):
                telegram = Telegram()
                telegram.user = user
                telegram.telegram_id = request.GET['id']
                telegram.save()
                return HttpResponse(True)
    return HttpResponse(False)

