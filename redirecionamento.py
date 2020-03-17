import requests

r = requests.get('http://www.google.com', allow_redirects=False)

print(r.history[0].headers['Location'])