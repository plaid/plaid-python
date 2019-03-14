Plaid Python Documentation!
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Client
------

.. currentmodule:: plaid

.. autoclass:: plaid.Client

    .. automethod:: __init__

API Endpoints
-------------

Many API endpoints accept optional parameters via an ``_options`` object in the
raw JSON. To improve forward compatibility as options are added, the Python
functions for these endpoints also include an ``_options`` argument. However,
it is recommended that you pass in options using the provided keyword
arguments where possible.

For example:

.. code-block:: python

  // Prefer this...
  client.Transactions.get(access_token,
                          start_date,
                          end_date,
                          account_ids=account_ids,
                          count=count,
                          offset=offset);

  // ... over this.
  client.Transactions.get(access_token,
                          start_date,
                          end_date,
                          _options={
                            'account_ids': account_ids,
                            'count': count,
                            'offset': offset,
                          });

.. automodule:: plaid.api
    :members:

Errors
------

.. automodule:: plaid.errors
    :members:
    :show-inheritance:
    :member-order: bysource


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
