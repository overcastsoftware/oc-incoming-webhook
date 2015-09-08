from django.conf.urls import patterns, url, include

from .views import WebHookView

urlpatterns = patterns('',
    url(r'^$', WebHookView.as_view()),
)