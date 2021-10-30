import json
from urllib.request import urlopen
# From "https://github.com/herval/yahoo-finance/issues/51"
# with urlopen("https://query1.finance.yahoo.com/v7/finance/quote?symbols=TLS.AX,MUS.AX") as response:
with urlopen("https://query1.finance.yahoo.com/v8/finance/chart/GOOG?range=1d&includePrePost=false&interval=2m&corsDomain=finance.yahoo.com&.tsrc=finance") as response:
    source = response.read()

# print(source)
data = json.loads(source) # Convert to python format
# print(json.dumps(data['chart']['result'][0]['timestamp'],indent=4))
print(len(data['chart']['result'][0]['timestamp']))

# usd_rates = dict()
#
# for item in data['list']['resources']:
#     name = item['resource']['fields']['name']
#     price = item['resource']['fields']['price']
#     usd_rates[name] = price
#
# print(50 * float(usd_rates['USD/INR']))
