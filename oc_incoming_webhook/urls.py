from django.conf.urls import url, include

from .views import WebHookView

urlpatterns = [
    url(r'^$', WebHookView.as_view()),
]
