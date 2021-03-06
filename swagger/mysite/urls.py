"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from mysite import settings
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from django.views.decorators.cache import never_cache
from ckeditor_uploader.views import browse, upload
from .yasg import urlpatterns as doc_urls



urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('profile/', include('userprofile.urls')),
    path('news/', include('news.urls')),
    path('forum/', include('forum.urls')),
    path('accounts/', include('accounts.urls')),
    

    #сторонние модули
    path('grappelli/', include('grappelli.urls')),
    url(r'^upload/', login_required(upload), name='ckeditor_upload'),
    url(r'^browse/', login_required(never_cache(browse)), name='ckeditor_browse'),
] 



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += doc_urls