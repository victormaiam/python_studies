import requests

url = 'http://www.submarino.com.br'

r = requests.get(url)
cookie = r.cookies.get_dict()

url = 'http://busca.submarino.com.br/busca.php?={0}'.format(busca)

r = requests.get(url, cookies=cookie)
with open ('submarino.html', 'w') as f:
    f.write(r.text)