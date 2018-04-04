from django.conf.urls import url
from loginsys import views as loginsys

urlpatterns = [
    url(r'^login/$', loginsys.login),
    url(r'^logout/$', loginsys.logout),
    url(r'^register/$', loginsys.register),
]