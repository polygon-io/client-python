import time

from polygon import WebSocketClient, STOCKS_CLUSTER


def my_custom_process_message(message):
    print("this is my custom message processing", message)


def my_custom_error_handler(ws, error):
    print("this is my custom error handler", error)


def my_custom_close_handler(ws):
    print("this is my custom close handler")


def main():
    key = 'your api key'
    my_client = WebSocketClient(STOCKS_CLUSTER, key, my_custom_process_message)
    my_client.run_async()

    my_client.subscribe("T.MSFT", "T.AAPL", "T.AMD", "T.NVDA")
    time.sleep(1)

    my_client.close_connection()


if __name__ == "__main__":
    main()
