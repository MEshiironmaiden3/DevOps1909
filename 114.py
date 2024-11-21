import requests

response = requests.get("https://digital.isracard.co.il/")
if response.status_code == 200:
    print("URL found")