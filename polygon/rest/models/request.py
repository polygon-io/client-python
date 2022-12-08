from typing import Dict, Optional

X_POLYGON_EDGE_ID = "X-Polygon-Edge-ID"
X_POLYGON_EDGE_IP_ADDRESS = "X-Polygon-Edge-IP-Address"
X_POLYGON_EDGE_USER_AGENT = "X-Polygon-Edge-User-Agent"

HEADER = "header"


class RequestOptionBuilder:
    def __init__(
        self,
        edge_id: Optional[str] = None,
        edge_ip_address: Optional[str] = None,
        edge_user: Optional[str] = None,
    ):
        """
        RequestOptionBuilder is a utility class to build polygon api options used in requests.
        :param edge_id: is a required Launchpad header. It identifies the Edge User requesting data
        :param edge_ip_address: is a required Launchpad header. It denotes the originating IP Address of the Edge User
        :param edge_user: is an optional Launchpad header. It denotes the originating UserAgent of the Edge User requesting data.
        """
        self.edge_headers: Dict[str, str] = {}
        self.__handle_edge_header_options(
            edge_id=edge_id, edge_ip_address=edge_ip_address, edge_user=edge_user
        )

    def __handle_edge_header_options(
        self,
        edge_id: Optional[str],
        edge_ip_address: Optional[str] = None,
        edge_user: Optional[str] = None,
    ):
        edge_headers = {}
        if edge_id is not None:
            edge_headers[X_POLYGON_EDGE_ID] = edge_id
        if edge_ip_address is not None:
            edge_headers[X_POLYGON_EDGE_IP_ADDRESS] = edge_ip_address
        if edge_user is not None:
            edge_headers[X_POLYGON_EDGE_USER_AGENT] = edge_user
        self.__set_edge_headers(edge_headers)

    def __set_edge_headers(self, headers: Dict[str, str]):
        self.edge_headers = headers

    def __add_to_edge_headers(self, **headers):
        for k, v in headers.items():
            self.edge_headers[k] = v

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
        self.__add_to_edge_headers(
            **{
                X_POLYGON_EDGE_ID: edge_id,
                X_POLYGON_EDGE_IP_ADDRESS: edge_ip_address,
            }  # object destructure is needed for correct key formatting.
        )
        return self

    def optional_edge_headers(
        self,
        user_agent: str,
    ):
        """
        edge_user_agent_header is used to add the optional X-Polygon-Edge-User-Agent key to the header dictionary
        :param user_agent: is an optional Launchpad header. It denotes the originating UserAgent of the Edge User requesting data.
        :return: RequestOptionBuilder
        """
        self.__add_to_edge_headers(
            **{
                X_POLYGON_EDGE_USER_AGENT: user_agent,
            }
        )
        return self
