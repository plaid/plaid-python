from plaid.api.api import API


class Institutions(API):
    '''
    Institutions endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#institutions>`__)
    '''

    def get(self, count, offset=0):
        '''
        Fetch all Plaid institutions, using /institutions/all.

        :param  int     count:      Number of institutions to fetch.
        :param  int     offset:     Number of institutions to skip.
        '''
        return self.client.post('/institutions/get', {
            'count': count,
            'offset': offset,
        })

    def get_by_id(self, institution_id, _options={}):
        '''
        Fetch a single institution by id.

        :param  str     institution_id:
        '''
        return self.client.post_public_key('/institutions/get_by_id', {
            'institution_id': institution_id,
            'options': _options,
        })

    def search(self, query, _options={}, products=None):
        '''
        Search all institutions by name.

        :param  str      query:     Query against the full list of
                                    institutions.
        :param  [str]    products:  Filter FIs by available products. Optional.
        '''
        return self.client.post_public_key('/institutions/search', {
            'query': query,
            'products': products,
            'options': _options,
        })
