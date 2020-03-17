import requests

url = 'https://unsplash.com/photos/XVaXbzQul90'

r = requests.get(url)

with open('img.jpg', 'wb') as f:
    f.write(r.content)