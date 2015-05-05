import django
from django.core.cache.backends.base import InvalidCacheBackendError
from distutils.version import StrictVersion


try:
    if StrictVersion(django.get_version()) >= StrictVersion('1.7'):
        from django.core.cache import get_cache
        cache = get_cache('debug-panel')
    else:
        from django.core.cache import caches
        cache = caches['debug-panel']
except InvalidCacheBackendError:
    from django.core.cache import cache
