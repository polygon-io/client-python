from polygon import RESTClient


def main():
    key = "your api key"
    client = RESTClient(key)

    resp = client.stocks_equities_daily_open_close("AAPL", "2018-03-02")
    print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")


if __name__ == '__main__':
    main()
