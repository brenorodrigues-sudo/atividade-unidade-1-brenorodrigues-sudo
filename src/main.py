# src/main.py

from leitor import ler_arquivo
from escritor import salvar_arquivo
from ordenacao import radix_sort

def main():
    print("=" * 60)
    print("🚀 Aplicação de Ordenação de Protocolos Iniciada")
    print("=" * 60)

    # Lista de arquivos que serão processados
    nomes = ["p-10.txt", "p-100.txt", "p-1000.txt", "p-100000.txt", "p-1000000.txt"]

    # Processa cada arquivo
    for nome in nomes:
        entrada = f"../data/{nome}"
        saida = f"../data/{nome.replace('.txt', '-ordenado.txt')}"

        print(f"\n📂 Lendo arquivo: {entrada}")
        protocolos = ler_arquivo(entrada)

        print(f"🔄 Ordenando {len(protocolos)} protocolos...")
        ordenados = radix_sort(protocolos)

        print(f"💾 Salvando resultado em: {saida}")
        salvar_arquivo(saida, ordenados)

        print(f"✅ Arquivo {nome} ordenado e salvo com sucesso!\n")

    print("=" * 60)
    print("🏁 Processamento finalizado com sucesso!")
    print("=" * 60)


if __name__ == "__main__":
    main()

