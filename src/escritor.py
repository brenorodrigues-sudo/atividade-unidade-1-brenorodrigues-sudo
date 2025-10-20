# src/escritor.py

def salvar_arquivo(caminho, lista):
    print(f"> Salvando {len(lista)} protocolos em {caminho}")
    arquivo = open(caminho, "w")
    for i in range(len(lista)):
        protocolo = lista[i]
        arquivo.write(str(protocolo) + "\n")
    arquivo.close()