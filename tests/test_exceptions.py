import unittest
import warnings

from plaid.exceptions import ApiException


class RawHttpResponse:
    status = 400
    reason = "Bad Request"
    data = b""
    headers = {"X-Test": "value"}

    def getheaders(self):
        warnings.warn(
            "HTTPResponse.getheaders() is deprecated",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.headers


class WrappedHttpResponse:
    status = 400
    reason = "Bad Request"
    data = b""

    def getheaders(self):
        return {"X-Test": "value"}


class ApiExceptionTest(unittest.TestCase):
    def test_raw_response_uses_headers_without_deprecated_getheaders(self):
        response = RawHttpResponse()

        with warnings.catch_warnings():
            warnings.simplefilter("error", DeprecationWarning)
            exception = ApiException(http_resp=response)

        self.assertEqual(exception.headers, response.headers)

    def test_wrapped_response_keeps_getheaders_fallback(self):
        exception = ApiException(http_resp=WrappedHttpResponse())

        self.assertEqual(exception.headers, {"X-Test": "value"})


if __name__ == "__main__":
    unittest.main()
