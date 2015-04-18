class PlaidError(Exception):
    """
    Base error class
    """
    def __init__(self, message, properties):
        super(PlaidError, self).__init__(message)

        self.safe = properties['safe']
        self.reconnection = properties['reconnection']
        

def build_api_error(retval):
    """
    Helper method for creating errors
    """
    code = retval.json()['code']
    print "[ERROR][PLAIDAPI] Received plaid error " + str(code)

    # Does this error indicate that user should reconnect their bank account?
    reconnection_codes = [
        1105,  # corrupted access token
        1200,  # invalid credentials
        1201,  # invalid username
        1202,  # invalid password
        1203,  # invalid mfa
        1215   # mfa patch
    ]

    # Is this the type of error user should receive notification about?
    notification_codes = [
        1205,  # account locked
        1206,  # account not set up
        1212,  # no accounts
        1210,  # account not supported
        1211   # account not supported (safepass)
    ]

    # Is this error built to have its message shown directly to a user?    
    safe_codes = [
        1203,  # invalid mfa
        1212,  # no accounts
        1207,  # country not supported
        1208,  # mfa not supported
        1209,  # invalid pin
        1210,  # account not supported
        1211,  # account not supported (safepass)
        1302,  # institution not responding
        1200,  # invalid credentials
        1201,  # invalid username
        1202,  # invalid password
        1303   # institution down
    ]

    properties = {
        'safe': False,
        'reconnection': False
    }

    if code in reconnection_codes:
        properties['reconnection'] = True

    if code in safe_codes:
        properties['safe'] = True

    # Custom messages
    if code == 1205:
        message = 'Your account is locked. Log into your bank\'s website to fix.'  
    elif code == 1206:
        message = 'Your account is not set up. Log into your bank\'s website to fix.'
    else:
        message = retval.json()['resolve']

    error = PlaidError(message, properties)
    raise error
