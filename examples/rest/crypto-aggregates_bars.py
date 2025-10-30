from massive import RESTClient

# docs
# https://massive.com/docs/crypto/get_v2_aggs_ticker__cryptoticker__range__multiplier___timespan___from___to
# https://massive-api-client.readthedocs.io/en/latest/Aggs.html#massive.RESTClient.list_aggs

# API key injected below for easy use. If not provided, the script will attempt
# to use the environment variable "MASSIVE_API_KEY".
#
# setx MASSIVE_API_KEY "<your_api_key>"   <- windows
# export MASSIVE_API_KEY="<your_api_key>" <- mac/linux
#
# Note: To persist the environment variable you need to add the above command
# to the shell startup script (e.g. .bashrc or .bash_profile.
#
# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

aggs = []
for a in client.list_aggs(
    "X:BTCUSD",
    1,
    "day",
    "2023-01-30",
    "2023-02-03",
    limit=50000,
):
    aggs.append(a)

print(aggs)
