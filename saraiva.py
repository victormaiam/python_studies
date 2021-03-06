import requests
from bs4 import BeautifulSoup

def get_http(url, nome_livro):

    nome_livro = nome_livro.replace(' ', '+')
    url = '{0}busca?q={1}'.format(url, nome_livro)

    try:
        return requests.get(url)
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        print(str(e))
        pass
    except Exception as e:
        raise

def get_url_produtos(content):

    soup = BeautifulSoup(content, 'lxml')
    produtos = soup.find_all('div', {'class': 'nm-search-results-container'})

    lista_produtos = []
    for produto in produtos:
        info_produto = [produto.a.get('href'), produto.a.string]
        lista_produtos.append(info_produto)
    return lista_produtos

if __name__ == '__main__':

    url = 'http://busca.saraiva.com.br/'
    nome_livro =  'redes de computadores'

    r = get_http(url, nome_livro)

    if r:
        lista_produtos = get_url_produtos(r.text)
        print(lista_produtos)

    with open('result.html', 'w') as f:
            f.write(r.text)
