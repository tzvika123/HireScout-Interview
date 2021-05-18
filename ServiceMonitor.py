import requests

r = None
while r == 200 or r == None:
    try:
        r = (requests.get("https://www.google.com/")).status_code
    except:
        r = 0
print("service is down")
