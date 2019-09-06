from plaid.api.api import API


class Institutions(API):
    '''
    Institutions endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#institutions>`__)
    '''

    def get(self, count, offset=0, _options=None, session=None):
        '''
        Fetch all Plaid institutions, using /institutions/all.

        :param  int     count:      Number of institutions to fetch.
        :param  int     offset:     Number of institutions to skip.
        :param  object  session:    A requests.Session instance to use for
                                    making HTTP requests. Optional.
        '''

        options = _options or {}

        return self.client.post('/institutions/get', {
            'count': count,
            'offset': offset,
            'options': options,
        }, session=session)

    def get_by_id(self, institution_id, _options=None, session=None):
        '''
        Fetch a single institution by id.

        :param  str     institution_id:
        :param  object  session:        A requests.Session instance to use for
                                        making HTTP requests. Optional.
        '''
        options = _options or {}

        return self.client.post('/institutions/get_by_id', {
            'institution_id': institution_id,
            'options': options,
        }, session=session)

    def search(self, query, _options=None, products=None, session=None):
        '''
        Search all institutions by name.

        :param  str      query:     Query against the full list of
                                    institutions.
        :param  [str]    products:  Filter FIs by available products. Optional.
        :param  object   session:   A requests.Session instance to use for
                                    making HTTP requests. Optional.
        '''
        options = _options or {}

        return self.client.post('/institutions/search', {
            'query': query,
            'products': products,
            'options': options,
        }, session=session)
