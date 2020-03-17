import requests

url = 'https://www.youtube.com/results?'

payload = {'search_query': 'python for begginers'}

#payload['search_query'] = 'como fazer estrogonofe de frango'
r = requests.get(url, params=payload)
print(r.text)