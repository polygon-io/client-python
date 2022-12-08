from polygon import RESTClient
from polygon.rest.models.request import RequestOptionBuilder


def getAggsLaunchpad():
    client = RESTClient()

    options = (
        RequestOptionBuilder()
        .required_edge_headers(edge_id="EDGE_ID", edge_ip_address="EDGE_ID_ADDRESS")
        .edge_user_agent_header(user_agent="EDGE_USER_AGENT")
    )

    trades = []
    for t in client.list_trades("AAA", "2022-04-04", limit=5, options=options):
        trades.append(t)
    print(trades)


def main():
    getAggsLaunchpad()


if __name__ == "__main__":
    main()
