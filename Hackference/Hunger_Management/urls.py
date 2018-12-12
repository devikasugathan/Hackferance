from django.conf.urls import url
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
urlpatterns = [

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('about/',TemplateView.as_view(template_name='about-us.html'),name='about'),
    path('contact/',TemplateView.as_view(template_name='contact.html'),name='contact'),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
]
