# -*- coding: utf-8 -*-
class LazyProperty(object):
    """
    LazyProperty
    explain: http://blog.khulnasoft.com/gatherproxy
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value
