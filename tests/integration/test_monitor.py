import time
import datetime

from plaid.model.client_user_id_nullable import ClientUserIDNullable
from plaid.model.generic_country_code_nullable import GenericCountryCodeNullable
from plaid.model.watchlist_screening_status import WatchlistScreeningStatus
from plaid.model.watchlist_screening_status_nullable import WatchlistScreeningStatusNullable
from plaid.model.watchlist_screening_document_value_nullable import WatchlistScreeningDocumentValueNullable
from plaid.model.watchlist_screening_individual_name import WatchlistScreeningIndividualName
from plaid.model.watchlist_screening_request_search_terms import WatchlistScreeningRequestSearchTerms

from plaid.model.watchlist_screening_individual_create_request import WatchlistScreeningIndividualCreateRequest
from plaid.model.watchlist_screening_individual_update_request import WatchlistScreeningIndividualUpdateRequest
from plaid.model.watchlist_screening_individual_list_request import WatchlistScreeningIndividualListRequest
from plaid.model.watchlist_screening_individual_get_request import WatchlistScreeningIndividualGetRequest

from tests.integration.util import create_client

WATCHLIST_PROGRAM_ID = "prg_egdF5fGjY8fWqk"
CLIENT_USER_ID = ClientUserIDNullable("monitor-user-" + str(time.time()))
LEGAL_NAME = WatchlistScreeningIndividualName("Domingo Huang")

def test_watchlist_screening_individual_create_and_update():
    client = create_client()

    document_number = WatchlistScreeningDocumentValueNullable("123456789")
    date_of_birth = datetime.date(1990, 1, 1)
    country_code = GenericCountryCodeNullable("US")
    create_request = WatchlistScreeningIndividualCreateRequest(
        client_user_id=CLIENT_USER_ID,
        search_terms=WatchlistScreeningRequestSearchTerms(
            watchlist_program_id=WATCHLIST_PROGRAM_ID,
            legal_name=LEGAL_NAME,
            country=country_code,
            date_of_birth=date_of_birth,
            document_number=document_number
        )
    )
    # create Monitor individual request
    create_response = client.watchlist_screening_individual_create(create_request)

    # assert on response
    assert create_response["search_terms"]["legal_name"] == LEGAL_NAME
    assert create_response["search_terms"]["document_number"] == document_number
    assert create_response["search_terms"]["date_of_birth"] == date_of_birth
    assert create_response["search_terms"]["country"] == country_code
    assert create_response["status"] == WatchlistScreeningStatus("cleared")

    pending_review = WatchlistScreeningStatusNullable("pending_review")
    update_request = WatchlistScreeningIndividualUpdateRequest(
        watchlist_screening_id=create_response["id"],
        status=pending_review
    )

    # update Monitor individual request
    update_response = client.watchlist_screening_individual_update(update_request)

    assert update_response["status"] == WatchlistScreeningStatus("pending_review")

def test_watchlist_screening_individual_list_and_get():
    client = create_client()

    list_request = WatchlistScreeningIndividualListRequest(
        watchlist_program_id=WATCHLIST_PROGRAM_ID,
        client_user_id=CLIENT_USER_ID
    )

    # list Monitor individuals request
    list_response = client.watchlist_screening_individual_list(list_request)

    assert len(list_response["watchlist_screenings"]) == 1

    get_request = WatchlistScreeningIndividualGetRequest(
        watchlist_screening_id=list_response["watchlist_screenings"][0]["id"]
    )

    # get Monitor individual request
    get_response = client.watchlist_screening_individual_get(get_request)

    assert get_response["search_terms"]["legal_name"] == LEGAL_NAME
