from functools import wraps

from django.core.cache import cache
from django.http import HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist


def _get_cache_key(prefix, *args, **kwargs):
    """
    Calculates cache key based on `args` and `kwargs`.
    `args` and `kwargs` must be instances of hashable types.
    """
    hash_args_kwargs = hash(tuple(kwargs.iteritems()) + args)
    return '{}_{}'.format(prefix, hash_args_kwargs)


def cache_method(func, prefix=''):
    """
    Cache result of function execution into the `self` object (mostly useful in models).
    Calculate cache key based on `args` and `kwargs` of the function (except `self`).
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        cache_key_prefix = prefix or '_cache_{}'.format(func.__name__)
        cache_key = _get_cache_key(cache_key_prefix, *args, **kwargs)
        if not hasattr(self, cache_key):
            setattr(self, cache_key, func(self))
        return getattr(self, cache_key)
    return wrapper


def cache_func(func, prefix=''):
    """
    Cache result of function execution into the django cache backend.
    Calculate cache key based on `args` and `kwargs` of the function.
    For using like object method use `method_decorator`.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = _get_cache_key(prefix if prefix else func.__name__, *args, **kwargs)
        cached_value = cache.get(cache_key)
        if cached_value is None:
            cached_value = func(*args, **kwargs)
            cache.set(cache_key, cached_value)
        return cached_value
    return wrapper


def get_or_default(func, default=None):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ObjectDoesNotExist:
            return default
    return wrapper


def ajax_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST' and request.is_ajax():
            return func(request, *args, **kwargs)
        return HttpResponseBadRequest()
    return wrapper
