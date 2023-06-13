from polygon import RESTClient

# docs
# https://polygon.io/docs/indices/get_v2_aggs_ticker__indicesticker__range__multiplier___timespan___from___to
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#polygon.RESTClient.list_aggs

# API key injected below for easy use. If not provided, the script will attempt
# to use the environment variable "POLYGON_API_KEY".
#
# setx POLYGON_API_KEY "<your_api_key>"   <- windows
# export POLYGON_API_KEY="<your_api_key>" <- mac/linux
#
# Note: To persist the environment variable you need to add the above command
# to the shell startup script (e.g. .bashrc or .bash_profile.
#
# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

aggs = []
for a in client.list_aggs(
    "I:SPX",
    1,
    "day",
    "2023-03-10",
    "2023-05-12",
    limit=50000,
):
    aggs.append(a)

print(aggs)
