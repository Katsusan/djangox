"""djangox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from Jared import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('index/', views.index_view),
	re_path(r'^page/(?P<pn>[0-9]+)/$', views.article_pages),
	re_path(r'^article/(?P<id>[0-9]+)/$', views.single_article),
	re_path(r'^api/articles/$', views.article_list),
	re_path(r'^api/article/(?P<pk>[0-9]+)/$', views.article_detail),
	re_path(r'^api/page/(?P<pg>[0-9]+)/$', views.article_by_page),
]

