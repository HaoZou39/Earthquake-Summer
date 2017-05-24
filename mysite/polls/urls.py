from django.conf.urls import url

from polls import views as polls_views

urlpatterns = [
    url(r'^$', polls_views.polls,name='polls'),
]