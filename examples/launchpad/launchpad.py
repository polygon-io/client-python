from polygon import RESTClient
from polygon.rest.models.request import RequestOptionBuilder


def get_aggs_launchpad():
    client = RESTClient()

    """
    options can be added to the RequestOptionBuilder both directly in 
    initialization 
    Example:
    `options = RequestOptionBuilder(edge_id="", edge_ip_address="")
    
    or you can use the builder patten
    Example:
    options = RequestOptionBuilder()
        .required_edge_headers(edge_id="EDGE_ID", edge_ip_address="EDGE_ID_ADDRESS")
        .optional_edge_headers(user_agent="EDGE_USER_AGENT")
    """
    options = (
        RequestOptionBuilder()
        .required_edge_headers(edge_id="EDGE_ID", edge_ip_address="EDGE_ID_ADDRESS")
        .optional_edge_headers(user_agent="EDGE_USER_AGENT")
    )

    trades = []
    for t in client.list_trades("AAA", "2022-04-04", limit=5, options=options):
        trades.append(t)
    print(trades)


def main():
    get_aggs_launchpad()


if __name__ == "__main__":
    main()
