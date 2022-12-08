from typing import Dict, Optional

X_POLYGON_EDGE_ID = "X-Polygon-Edge-ID"
X_POLYGON_EDGE_IP_ADDRESS = "X-Polygon-Edge-IP-Address"
X_POLYGON_EDGE_USER_AGENT = "X-Polygon-Edge-User-Agent"

HEADER = "header"


class RequestOptionBuilder:
    def __init__(
        self,
        options: Optional[Dict[str, Dict[str, str]]] = None,
        edge_headers: Optional[Dict[str, str]] = None,
    ):
        """
        RequestOptionBuilder is a utility class used to format and produce options for Polygon Requests\
        :param options: preset options object to be the base of the options dictionary.
        :param options: preset options for launchpad edge headers
        """
        self.options = {} if options is None else options
        self.edge_headers = {} if edge_headers is None else edge_headers

    def __set_edge_headers(self, headers: Dict[str, str]):
        self.edge_headers = headers

    def __add_to_options(self, key: str, **options):
        """
        __add_to_options is a utility method used to add dicts and values
        to the options' dictionary.
        :param key: name of the dict a user is adding values to
        :param options: values to be added to specified dict
        :return: RequestOptionBuilder
        """
        if key not in self.options:
            self.options[key] = {}

        for k, v in options.items():
            self.options[key][k] = v

        # python 3.8 does not support match case...
        if key == HEADER:
            self.__set_edge_headers(options[key])

    def required_edge_headers(
        self,
        edge_id: str,
        edge_ip_address: str,
    ):
        """
        require_edge_headers adds required headers to the headers' dictionary
        :param edge_id: is a required Launchpad header. It identifies the Edge User requesting data
        :param edge_ip_address: is a required Launchpad header. It denotes the originating IP Address of the Edge User
        requesting data.
        :return: RequestOptionBuilder
        """
        self.__add_to_options(
            key=HEADER,
            X_POLYGON_EDGE_ID=edge_id,
            X_POLYGON_EDGE_IP_ADDRESS=edge_ip_address,
        )
        return self

    def edge_user_agent_header(
        self,
        user_agent: str,
    ):
        """
        edge_user_agent_header is used to add the optional X-Polygon-Edge-User-Agent key to the header dictionary
        :param user_agent: is an optional Launchpad header. It denotes the originating UserAgent of the Edge User requesting data.
        :return: RequestOptionBuilder
        """
        self.__add_to_options(
            key=HEADER,
            X_POLYGON_EDGE_USER_AGENT=user_agent,
        )
        return self
