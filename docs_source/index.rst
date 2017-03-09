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
  client.Item.create(credentials=dict(username='user_good',
                                      password='pass_good'),
                     institution_id='ins_109508',
                     initial_products=['transactions', 'numbers'],
                     webhook='https://example.com/webhook');

  // ... over this.
  client.Item.create(credentials=dict(username='user_good',
                                      password='pass_good'),
                     institution_id='ins_109508',
                     initial_products=['transactions', 'numbers'],
                     _options={
                     	'webhook': 'https://example.com/webhook',
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
