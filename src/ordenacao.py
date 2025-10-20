# src/ordenacao.py

def radix_sort(protocolos):
    if not protocolos:
        return protocolos

    tamanho = len(protocolos[0].chave())

    for pos in range(tamanho - 1, -1, -1):
        protocolos = counting_sort_por_posicao(protocolos, pos)

    return protocolos

def counting_sort_por_posicao(lista, pos):
    n = len(lista)
    saida = [None] * n
    contagem = [0] * 256 

  
    for i in range(n):
        chave = lista[i].chave()
        caractere = ord(chave[pos]) 
        contagem[caractere] += 1


    for i in range(1, 256):
        contagem[i] += contagem[i - 1]

    
    for i in range(n - 1, -1, -1):
        chave = lista[i].chave()
        caractere = ord(chave[pos])
        contagem[caractere] -= 1
        saida[contagem[caractere]] = lista[i]

    return saida
