import unittest

from polygon import RESTClient
from polygon.rest.models.request import (
    RequestOptionBuilder,
    X_POLYGON_EDGE_ID,
    X_POLYGON_EDGE_USER_AGENT,
    X_POLYGON_EDGE_IP_ADDRESS,
)


class RequestTest(unittest.TestCase):
    def test_empty_request_options(self):
        options = RequestOptionBuilder()

        expected_edge_headers = {}
        assert expected_edge_headers == options.edge_headers

    def test_request_options_with_initialized_values(self):
        options = RequestOptionBuilder(
            edge_id="test", edge_ip_address="test", edge_user="test"
        )

        expected_object = {
            X_POLYGON_EDGE_ID: "test",
            X_POLYGON_EDGE_IP_ADDRESS: "test",
            X_POLYGON_EDGE_USER_AGENT: "test",
        }

        assert expected_object == options.edge_headers

    def test_request_options_builder(self):
        options = RequestOptionBuilder().required_edge_headers(
            edge_id="test", edge_ip_address="test"
        )

        required_options = {
            X_POLYGON_EDGE_ID: "test",
            X_POLYGON_EDGE_IP_ADDRESS: "test",
        }
        print(options.edge_headers, required_options)
        self.assertDictEqual(required_options, options.edge_headers)

        all_options = {
            X_POLYGON_EDGE_ID: "test",
            X_POLYGON_EDGE_IP_ADDRESS: "test",
            X_POLYGON_EDGE_USER_AGENT: "test",
        }

        options = options.optional_edge_headers("test")
        self.assertDictEqual(all_options, options.edge_headers)

    def test_header_combination(self):
        client = RESTClient(api_key="test")
        options = RequestOptionBuilder(
            edge_id="test", edge_ip_address="test", edge_user="test"
        )

        # this mocks the expected behavior during the request.get function call
        # in the BaseClient.
        headers = client._concat_headers(options.edge_headers)

        expected_headers = {
            "Authorization": "Bearer test",
            "User-Agent": "Polygon.io PythonClient/0.0.0",
            "X-Polygon-Edge-ID": "test",
            "X-Polygon-Edge-IP-Address": "test",
            "X-Polygon-Edge-User-Agent": "test",
        }

        self.assertDictEqual(headers, expected_headers)
