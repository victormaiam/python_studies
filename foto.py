import requests

url = 'https://unsplash.com/photos/Y6I4VvyN_sA'

r = requests.get(url)

with open('img.jpg', 'wb') as f:
    f.write(r.content)