__all__ = ['urljoin', 'urlencode']

try:
    from urllib.parse import urljoin, urlencode
except ImportError:
    from urllib import urlencode
    from urlparse import urljoin
