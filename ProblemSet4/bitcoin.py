import requests
import sys
import json

try:
    try:
        x = float(sys.argv[1])
    except ValueError:
        print("arg not convertable")
        sys.exit()

    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(f"{(float(request.json()['bpi']['EUR']['rate'].replace(',','')) * x):,.4f}")
except requests.RequestException:
    print("bad api call")
    sys.exit()