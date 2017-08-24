from plaid.api.api import API


class Transactions(API):
    '''Transactions endpoints.'''

    def get(self,
            access_token,
            start_date,
            end_date,
            _options={},
            account_ids=None,
            count=None,
            offset=None,
            ):
        '''
        Return accounts and transactions for an item.
        (`HTTP docs <https://plaid.com/docs/api/#transactions>`__)

        The transactions in the response are paginated -- compare the number of
        transactions received so far against response['total_transactions'] to
        determine whether to fetch another page.

        :param  str     access_token:
        :param  str     start_date:     The earliest date for transactions.
        :param  str     end_date:       The latest date for transactions.
        :param  [str]   account_ids:    A list of account_ids to retrieve for
                                        the item. Optional.
        :param  int     count:          The number of transactions to fetch.
                                        Optional.
        :param  int     offset:         The number of transactions to skip from
                                        the beginning of the fetch. Optional.

        All date should be formatted as ``YYYY-MM-DD``.
        '''
        options = {}
        options.update(_options)
        if account_ids is not None:
            options['account_ids'] = account_ids
        if count is not None:
            options['count'] = count
        if offset is not None:
            options['offset'] = offset

        return self.client.post('/transactions/get', {
            'access_token': access_token,
            'start_date': start_date,
            'end_date': end_date,
            'options': options,
        })
