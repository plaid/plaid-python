__all__ = ['json', 'urljoin', 'urlencode']


json = None

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise ImportError('Plaid depends on a JSON library')
finally:
    if not hasattr(json, 'loads'):
        raise ImportError(
            'JSON library incompatible with the Plaid API client'
        )

try:
    from urllib.parse import urljoin, urlencode
except ImportError:
    from urllib import urlencode
    from urlparse import urljoin


def to_json(response):
    return json.loads(response.text)
