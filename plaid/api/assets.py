from plaid.api.api import API


class AssetReport(API):
    '''Assets endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#assets>`__)'''

    def __init__(self, client):
        super(AssetReport, self).__init__(client)
        self.audit_copy = AuditCopy(client)

    def create(self,
               access_tokens,
               days_requested,
               options={}):
        '''
        Create an asset report.

        :param  [str]   access_tokens:  A list of access tokens, one token for
                                        each Item to be included in the Asset
                                        Report.
        :param  int     days_requested: Days of transaction history requested
                                        to be included in the Asset Report.
        :param  dict    options:        An optional dictionary. For more
                                        information on the user object, see
                                        the documentation site listed above.
        '''

        return self.client.post('/asset_report/create', {
            'access_tokens': access_tokens,
            'days_requested': days_requested,
            'options': options,
        })

    def get(self,
            asset_report_token):
        '''
        Retrieves an asset report.

        :param  str   asset_report_token:   The asset report token for the
                                            asset report you created.
        '''

        return self.client.post('/asset_report/get', {
            'asset_report_token': asset_report_token,
        })

    def get_pdf(self,
                asset_report_token):
        '''
        Retrieves an asset report in the PDF format.

        :param  str   asset_report_token:   The asset report token for the
                                            asset report you created.
        '''

        return self.client.post('/asset_report/pdf/get', {
            'asset_report_token': asset_report_token,
        }, is_json=False)

    def remove(self,
               asset_report_token):
        '''
        Retrieves an asset report in the PDF format.

        :param  str   asset_report_token:   The asset report token for the
                                            asset report you want to remove.
        '''

        return self.client.post('/asset_report/remove', {
            'asset_report_token': asset_report_token,
        })


class AuditCopy(API):
    '''Audit copy endpoints. Use this class via the `audit_copy` member on the
    `AssetReport` class.'''

    def create(self,
               asset_report_token,
               auditor_id):
        '''
        Creates an audit copy.

        :param  str   asset_report_token:   The asset report token for the
                                            asset report you created.
        :param  str   auditor_id:           The ID of the third party with
                                            which you want to share the asset
                                            report.

        '''

        return self.client.post('/asset_report/audit_copy/create', {
            'asset_report_token': asset_report_token,
            'auditor_id': auditor_id,
        })

    def remove(self,
               audit_copy_token):
        '''
        Removes an audit copy.

        :param  str   audit_copy_token:     The audit copy token for the
                                            audit copy you want to remove.

        '''

        return self.client.post('/asset_report/audit_copy/remove', {
            'audit_copy_token': audit_copy_token,
        })
