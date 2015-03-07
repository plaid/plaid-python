class PlaidSafeError(Exception):
	"""
	Denotes a plaid error that has a message which is safe to return
	directly to the user
	"""
    pass