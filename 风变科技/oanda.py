import requests,time

respone = requests.get("https://www1.oanda.com/currency/converter/")
print(respone.status_code)