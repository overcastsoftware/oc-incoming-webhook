import logging

from django.http import HttpResponse
from django.views.generic import View

from django.views.decorators.csrf import csrf_exempt
from .signals import web_hook_signal


class WebHookView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(WebHookView, self).dispatch(*args, **kwargs)

    def post(self, request):
        if request.method == "POST":
            payload = request.POST.dict()
            web_hook_signal.send(WebHookView, request=request, payload=payload)

        return HttpResponse("OK")