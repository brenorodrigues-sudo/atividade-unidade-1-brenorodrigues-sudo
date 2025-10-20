# Atividade de Ordenação – Estrutura de Dados e Algoritmos 1

## Objetivo

Foi desenvolvido um sistema em Python capaz de realizar a ordenação de grandes volumes de protocolos, com base em três critérios hierárquicos:

1. **Ano** (em ordem crescente)
2. **Tipo** (em ordem lexicográfica crescente)
3. **Número** (em ordem crescente, mantendo zeros à esquerda)


---

##  Algoritmo de Ordenação Escolhido: **Radix Sort**

###  Critérios de Escolha

O algoritmo **Radix Sort** foi escolhido por ser um algoritmo de ordenação **não comparativo**, ideal para casos onde:

- Os elementos possuem **formato fixo e bem estruturado** (número-tipo-ano);
- O número de comparações diretas pode ser evitado;
- A ordenação precisa ser **estável** e **eficiente** com entradas muito grandes.

Radix Sort, nesse contexto, supera algoritmos como Bubble Sort (`O(n²)`), Insertion Sort (`O(n²)`), e até Merge Sort (`O(n log n)`), porque explora diretamente a estrutura dos dados em múltiplos passes (por dígito/caractere).

---

## 📐 Complexidade Teórica

A complexidade do algoritmo Radix Sort é: `O(nk)`



Onde:
- `n` é o número de elementos.
- `k` é o número de dígitos/caracteres por chave.
- Então `k` é constante, resultando em uma complexidade **linear O(n)**.


