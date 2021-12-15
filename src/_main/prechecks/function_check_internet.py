def ping_internet(url="https://www.google.com/"):
    # Checks for the internet
    internet = True
    try:
        import requests as r
        web = r.get(url).status_code
    except r.ConnectionError:
        internet = False
    return internet

print(ping_internet())
