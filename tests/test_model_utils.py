import json
import unittest

from plaid.model.country_code import CountryCode
from plaid.model.depository_account_subtype import DepositoryAccountSubtype
from plaid.model.depository_account_subtypes import DepositoryAccountSubtypes
from plaid.model.depository_filter import DepositoryFilter
from plaid.model.link_token_account_filters import LinkTokenAccountFilters
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_auth import LinkTokenCreateRequestAuth
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products


class ModelToDictTest(unittest.TestCase):
    def test_nested_simple_model_list_is_json_serializable(self):
        request = LinkTokenCreateRequest(
            client_name="test",
            country_codes=[CountryCode("US")],
            language="en",
            products=[Products("auth"), Products("transactions")],
            user=LinkTokenCreateRequestUser(client_user_id="1234"),
            account_filters=LinkTokenAccountFilters(
                depository=DepositoryFilter(
                    account_subtypes=DepositoryAccountSubtypes(
                        [DepositoryAccountSubtype(value="checking")]
                    )
                )
            ),
            auth=LinkTokenCreateRequestAuth(instant_match_enabled=True),
        )

        result = request.to_dict()

        self.assertEqual(
            result["account_filters"]["depository"]["account_subtypes"],
            ["checking"],
        )
        self.assertEqual(json.loads(json.dumps(result)), result)


if __name__ == "__main__":
    unittest.main()
