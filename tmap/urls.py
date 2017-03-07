from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name='tmap'
urlpatterns = [
        url(r'^$', views.index, name='index'),
]
