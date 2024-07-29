from polygon import RESTClient
import json


def get_related_tickers():
    client = RESTClient(trace=True)

    # Fetch a limited list of tickers to keep the example manageable
    main_tickers = ["MSFT", "AMZN", "META", "AAPL", "GOOG", "NVDA", "TSLA", "DIS"]

    # Prepare data structures for nodes and edges
    nodes = []
    edges = []
    id_map = {}
    current_id = 1

    # Iterate over each main ticker and find related tickers
    for ticker in main_tickers:
        if ticker not in id_map:
            id_map[ticker] = current_id
            nodes.append({"id": current_id, "label": ticker})
            current_id += 1

        related_companies = client.get_related_companies(ticker)
        for company in related_companies:
            related_ticker = company.ticker
            if related_ticker not in id_map:
                id_map[related_ticker] = current_id
                nodes.append({"id": current_id, "label": related_ticker})
                current_id += 1

            edges.append({"from": id_map[ticker], "to": id_map[related_ticker]})

    # Save the nodes and edges to a JSON file for web visualization
    with open("data.json", "w") as f:
        json.dump({"nodes": nodes, "edges": edges}, f)


if __name__ == "__main__":
    get_related_tickers()
