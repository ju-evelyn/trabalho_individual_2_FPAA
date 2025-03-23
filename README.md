# Projeto Algoritmo de Seleção Simultânea do  Maior e do Menor Elementos (MaxMin Select)
## Sobre o Algoritmo
Objetivo:
-  Desenvolver um programa em Python que implemente o algoritmo de seleção simultânea do maior e do menor elementos (MaxMin Select) de uma sequência de números, utilizando a abordagem de divisão e conquista.

Sobre o algoritmo:
- O algoritmo de seleção simultânea (MaxMin Select) pode ser implementado de forma recursiva, utilizando a técnica de divisão e conquista. O problema é dividido em subproblemas menores que são resolvidos recursivamente, e seus resultados são combinados para encontrar o maior e o menor elementos com eficiência. Esse método reduz o número de comparações necessárias em comparação com uma abordagem ingênua

## Como executar o projeto
### Passo 1: Criar e ativar o ambiente virtual
É recomendável usar um ambiente virtual para gerenciar suas dependências. Siga os passos abaixo para configurar um ambiente virtual:

1.  Crie um ambiente virtual usando o seguinte comando:
    `python3 -m venv .venv`

2.  Ative o ambiente virtual:
    -   No macOS e Linux: `source .venv/bin/activate`
    -   No Windows: `.venv\Scripts\activate`

### Passo 2: Executar o script
Após ativar o ambiente virtual, execute o script principal: `python main.py`

### Versão do Python
Este projeto foi desenvolvido na versão  **3.13.2**  do Python e  **não exige a instalação de nenhuma dependência adicional**.

## Lógica do algoritmo implementado
#### Linha 1
O algoritmo inicia com a função `max_min_select(arr)` recebendo uma sequência de números
#### Linhas 2 a 9 (base da recursão)
Nesse bloco é feito uma validação se o array possui 1 ou 2 dígitos, retornando que o maior e o menor número é ele mesmo no caso de 1 número, ou fazendo uma comparação simples no caso do array de 2 dígitos.
#### Linhas 12 a 13 (divisão)
A linha 12 seleciona o valor que representa a metade do array, e as linhas 13 e 14 alimentam as variáveis `left_max, left_min, right_max e right_min` chamando a recursão do método mara a parte esquerda do array e para a parte direita.
O método sempre retorna um conjunto de variáveis que representam o maior e o menor número.
#### Linhas 17 e 18 (conquista)
Nessas linhas são calculados o maior número dos 2 retornados em `left_max e right_max` , assim como o menor número entre `left_min e right_min`.

#### Linha 20
Por fim, é retornado o maior e o menor número do array passado inicialmente

## Relatório técnico
### Análise da complexidade assintótica
1.  **Contagem de Comparações:**

    -   No nível da recursão, existem subproblemas, cada um com tamanho .

    -   O número total de comparações pode ser descrito pela recorrência:
        
    `C(n) = 2C(n/2) + 2`

A complexidade é **O(n)**

### Aplicação do Teorema Mestre

A recorrência do MaxMin Select é dada por:

    T(n) = 2T(n/2) + O(1)

1.  Identificação dos parâmetros:

    -  a = 2: duas chamadas recursivas.
    -  b = 2: cada chamada recursiva trata um subproblema de tamanho .
    -  f(n) = O(1): o custo da combinação dos resultados é constante.

Portanto, a complexidade assintótica do MaxMin Select é: **O(n)**
 
