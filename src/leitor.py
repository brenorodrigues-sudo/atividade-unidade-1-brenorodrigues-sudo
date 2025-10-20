# src/leitor.py

from protocolo import Protocolo

def ler_arquivo(caminho):
    protocolos = []

    with open(caminho, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if linha != "":
                numero, tipo, ano = linha.split("-")
                protocolo = Protocolo(numero, tipo, ano)
                protocolos.append(protocolo)

    return protocolos
