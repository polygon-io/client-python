from polygon import RESTClient
from polygon.rest.models.request import RequestOptionBuilder


def get_aggs_launchpad():
    client = RESTClient()

    """
    options can be added to the RequestOptionBuilder both directly in 
    initialization 
    Example:
    `options = RequestOptionBuilder(edge_id="", edge_ip_address="")
    
    or you can use the builder patten for future modifications to 
    underlying edge header dictionary.
    Example:
    options = RequestOptionBuilder()
        .edge_headers(edge_id="EDGE_ID", edge_ip_address="EDGE_ID_ADDRESS")
        .update(edge_id="NEW")
    options = options.update_edge_header(edge_ip_address="NEW_IP")
    """
    options = (
        RequestOptionBuilder()
        .edge_headers(edge_id="EDGE_ID", edge_ip_address="EDGE_ID_ADDRESS")
        .update_edge_header(edge_user="EDGE_USER")
    )

    trades = []
    for t in client.list_trades("AAA", "2022-04-04", limit=5, options=options):
        trades.append(t)
    print(trades)


def main():
    get_aggs_launchpad()


if __name__ == "__main__":
    main()
