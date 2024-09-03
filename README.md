# Projeto de Testes Técnicos em Python

Este repositório contém soluções para desafios técnicos em Python. Cada desafio é implementado em um arquivo separado, e o projeto está organizado para que você possa executar cada desafio a partir de um menu principal. Abaixo estão os enunciados de cada desafio.

## Desafios

### 1. Sequência de Fibonacci

**Enunciado:**

Dada a sequência de Fibonacci, onde se inicia por 0 e 1, e o próximo valor sempre será a soma dos dois valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa em Python onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não à sequência.

**Como executar:**

Este desafio está implementado no arquivo `desafio1_fibonacci.py`. Para executar, escolha a opção 1 no menu principal.

### 2. Verificação de Letra 'a' em String

**Enunciado:**

Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

**Como executar:**

Este desafio está implementado no arquivo `desafio2_letra_a.py`. Para executar, escolha a opção 2 no menu principal.

### 3. Valor Final de Variável em Código

**Enunciado:**

Observe o trecho de código abaixo:

```python
int INDICE = 12, SOMA = 0, K = 1;

enquanto K < INDICE faça {
    K = K + 1;
    SOMA = SOMA + K;
}

imprimir(SOMA);
