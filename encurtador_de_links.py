import pyshorteners

def url():

    print('='*20)
    print('encurtador_de_links')
    print('='*20)
    print(end='\n')

    url = input('Digite o link do site: ')

    # Carrega lib #
    s = pyshorteners.Shortener()

    # Gera URL encurtada #
    shortUrl = s.tinyurl.short(url)

    # Mostra resultado #
    print(f"URL Encurtada: {shortUrl}")

url()

while True:
    retorno = str(input('Deseja encurtar outro link?\n [S] para sim\n [N] para não\n')).upper()

    if retorno == 'S':
            url()

    if retorno == 'N':
        exit()

    else:
        exit()
