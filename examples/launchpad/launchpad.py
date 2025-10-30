from massive import RESTClient
from massive.rest.models.request import RequestOptionBuilder


def get_list_trades_launchpad():
    client = RESTClient()

    """
    set headers example:
    options = RequestOptionBuilder()
        .edge_headers(edge_id="EDGE_ID", edge_ip_address="EDGE_ID_ADDRESS", edge_user="EDGE_USER")
        
    update headers example:
    options = options.update_edge_header(edge_ip_address="NEW_IP")
    """
    options = RequestOptionBuilder().edge_headers(
        edge_id="EDGE_ID", edge_ip_address="EDGE_ID_ADDRESS", edge_user="EDGE_USER"
    )

    trades = []
    for t in client.list_trades("AAA", "2022-04-04", limit=5, options=options):
        trades.append(t)
    print(trades)


def main():
    get_list_trades_launchpad()


if __name__ == "__main__":
    main()
