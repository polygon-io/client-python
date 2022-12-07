from typing import Dict

X_POLYGON_EDGE_ID = "X-Polygon-Edge-ID"
X_POLYGON_EDGE_IP_ADDRESS = "X-Polygon-Edge-IP-Address"
X_POLYGON_EDGE_USER_AGENT = "X-Polygon-Edge-User-Agent"


def add_headers_to_options(options: Dict[str, str], **headers) -> Dict[str, str]:
    if options is None:
        options = {}
    if "headers" not in options:
        options["headers"] = {}

    for k, v in headers.items():
        options["headers"][k] = v

    return options


def required_edge_headers(options: Dict[str, str], edge_id: str, edge_ip_address: str) -> Dict[str, str]:
    return add_headers_to_options(options, **{
        X_POLYGON_EDGE_ID: edge_id,
        X_POLYGON_EDGE_IP_ADDRESS: edge_ip_address,
    })


def edge_user_agent(options: Dict[str, str], user_agent: str) -> Dict[str, str]:
    return add_headers_to_options(options, **{
        X_POLYGON_EDGE_USER_AGENT: user_agent
    })
