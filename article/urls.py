from django.conf.urls import include, url
from article import views as articleViews

urlpatterns = [
    url(r'^articles/all/$', articleViews.articles),
    url(r'^articles/get/(?P<article_id>\d+)/$', articleViews.article),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', articleViews.addlike),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', articleViews.addcomment),
    url(r'^page/(\d+)/$', articleViews.articles),
    url(r'^$', articleViews.articles),
]
