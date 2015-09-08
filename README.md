Incoming webhook signal
=======================

A simple app to provide a webhook url and a signal that you can hook into.


Examples
--------

The following snippet show how to connect the webhook to a method using django's signal mechanism.
Note that path must be set to "send-signal" in the hook object instead of an absolute path to a script.


```
#!python
    from oc_incoming_webhook.signals import web_hook_signal

    def process_web_hook(sender, **kwargs):
        for key, value in kwargs.iteritems():
            print key, value
    
    web_hook_signal.connect(process_web_hook)
```