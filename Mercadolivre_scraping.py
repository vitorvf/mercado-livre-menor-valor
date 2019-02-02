import urllib.request
import bs4 as bs

def pesquisar(produto, menorpreco):
#produto = "microondas" foi apagado!
url = "https://lista.mercadolivre.com.br/{}".format(produto)
print("acessando site...")
pagina = urllib.request.urlopen(url)  # pegando código da pagina
codigo_pagina = bs.BeautifulSoup(pagina, features="html.parser")
print("Pesquisando produtos...")
itens = codigo_pagina.find_all('span', attrs={'class': 'price__fraction'})
links = codigo_pagina.find_all('a', attrs={'class': 'item__info-title'})

menor = 300
pocisao = 0
volta = 0
for i in itens:
    valor = float(i.text.strip().replace('.',""))
    if valor < menor:
        menor = valor
        posicao = volta
    volta = volta + 1
print("O produto mais barato custa :",menor)
print("Link do produto abaixo!")
print(links[posicao].get('href'))

if __name__= "__main__"
    # Se eu quiser executar no mesmo arquivo eu coloco
    #Pesquisar("microondas", 300)