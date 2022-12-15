from plaid.model.transactions_enrich_get_request import TransactionsEnrichGetRequest
from plaid.model.client_provided_transaction import ClientProvidedTransaction
from plaid.model.enrich_transaction_direction import EnrichTransactionDirection
from plaid.model.client_provided_transaction_location import ClientProvidedTransactionLocation

from tests.integration.util import create_client

SAMPLE_TRANSACTIONS_TO_ENRICH = [
    ClientProvidedTransaction(
        id="1",
        description="DDA PURCHASE *XXXX XXXXXXXX FAMILY DOLLAR",
        amount=10.21,
        iso_currency_code="USD",
        location=ClientProvidedTransactionLocation(
            city="Philadelphia",
            region="PA",
        ),
        direction=EnrichTransactionDirection(value="OUTFLOW")
    ),
    ClientProvidedTransaction(
        id="2",
        description="PURCHASE JUNIATA SUPE PHILADELPHIA PA CARDXXXX",
        amount=45.14,
        iso_currency_code="USD",
        direction=EnrichTransactionDirection(value="OUTFLOW")
    ),
    ClientProvidedTransaction(
        id="3",
        description="DEBIT CARD PURCHASE",
        amount=25.15,
        iso_currency_code="USD",
        direction=EnrichTransactionDirection(value="OUTFLOW")
    ),
    ClientProvidedTransaction(
        id="4",
        description="DIRECT DEP* UBER.COM",
        amount=250.15,
        iso_currency_code="USD",
        direction=EnrichTransactionDirection(value="INFLOW")
    ),
]


def test_enrich_transactions_success():
    client = create_client()

    enrich_req = TransactionsEnrichGetRequest(
        account_type="depository",
        transactions=SAMPLE_TRANSACTIONS_TO_ENRICH
    )

    response = client.transactions_enrich(enrich_req)

    enriched_transactions = response['enriched_transactions']
    assert len(enriched_transactions) == len(SAMPLE_TRANSACTIONS_TO_ENRICH)

    for item in enriched_transactions:
        for key in [
            'amount',
            'description',
            'direction',
            'enrichments',
            'id',
        ]:
            assert key in item
