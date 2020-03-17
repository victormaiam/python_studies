import requests 

#http://www.ultraproxies.com/
url = 'https://www.hide-my-ip.com/pt/proxylist.shtml'

proxies = {'http:139.59.62.255:8080'}

try:
    r = requests.get(url, proxies=proxies)
    print(r.status_code)
except requests.exceptions.ConnectionError as e:
    print(str(e))