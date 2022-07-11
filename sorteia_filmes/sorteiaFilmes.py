from random import choices

def sorteiaFilmes():
    try:
        lista = []
        txt = './filmes.txt'
        f = open(txt, 'r')
        for linha in f.readlines():
            name = linha.replace('\n', '')
            lista.append(name)
            print(f'Adicionado ao sorteio: {name}')
        f.close
        return print(f'Filme sorteado: {choices(lista)[0]}')
    except:
        print('Arquivo filmes.txt não encontrado.')

sorteiaFilmes()
