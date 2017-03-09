class API(object):
    '''Base class for classes containing groups of API endpoints.'''

    def __init__(self, client):
        self.client = client
