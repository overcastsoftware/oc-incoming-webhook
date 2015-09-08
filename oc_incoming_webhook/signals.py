from django import dispatch

class WebHookSignal(dispatch.Signal):
    pass

web_hook_signal = WebHookSignal()