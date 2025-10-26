# Guia Completo de Lógica de Programação com Python


A Lógica de Programação é a base fundamental para qualquer programador. Ela consiste na arte de estruturar o pensamento de forma sequencial, clara e eficiente para resolver problemas de maneira que um computador consiga executar.

# Parte 1: A Base - Algoritmo e Lógica

## 1. O que é Algoritmo?

Um Algoritmo é um conjunto finito e ordenado de passos não ambíguos (claros) que visam resolver um problema ou executar uma tarefa.

Exemplo Clássico (Algoritmo do Café):

- Pegar o pó de café.
- Colocar o pó no filtro.
- Colocar água para ferver.
- Quando a água ferver, despejá-la lentamente sobre o pó.
- Esperar o café coar.
- Servir.

Para a programação, o algoritmo precisa ser traduzido para uma linguagem que o computador entenda.

## 2. Representação de Algoritmos

Antes de codificar em Python, é crucial planejar o algoritmo usando uma das seguintes formas:

- Linguagem Natural (Descrição Narrativa): Usar o português (ou outra língua) de forma estruturada. Bom para o planejamento inicial.
- Fluxograma: Uma representação gráfica padronizada usando símbolos para mostrar o fluxo de controle.
- Pseudocódigo (Portugol): Uma representação textual intermediária, que se assemelha a uma linguagem de programação, mas usa termos da língua natural. É o mais usado para estruturar a lógica antes da codificação final.

Exemplo em Pseudocódigo (Calcular média.)

<img width="302" height="239" alt="image" src="https://github.com/user-attachments/assets/4cec6e92-fb22-4e62-a12d-9a6d184b9972" />

## 3. A Lógica em Ação: Conceitos Fundamentais

   
A lógica é implementada na programação através de conceitos universais, que em Python são traduzidos em sintaxes específicas.

# Parte 2: Fundamentos da Programação em Python

Vamos traduzir os conceitos lógicos para a sintaxe do Python.

## 1. Variáveis e Tipos de Dados.

Uma variável é um "endereço na memória" para guardar um valor. Python é dinamicamente tipado.

<img width="693" height="231" alt="image" src="https://github.com/user-attachments/assets/d86295d6-3ad4-402f-a8f5-72cdcaa6e469" />

### Atribuição e Entrada de Dados em Phyton:

#Atribuição (usamos = )  
altura = 1.75  # float  
nome = "João"  # str  

#Entrada de dados (usamos input())  
#O input() sempre retorna uma string, precisamos converter (casting) para número se for o caso  
nota1_str = input("Digite a primeira nota: ")  
nota1 = float(nota1_str) # Conversão de string para float  

#Saída de dados (usamos print())  
print("Olá,", nome)  
print(f"Sua nota é: {nota1}") # Usando f-string  

## 2. Expressões e Operadores

Expressões são combinações de valores, variáveis e operadores que resultam em um valor.

### Operadores Aritméticos em Python:

<img width="457" height="275" alt="image" src="https://github.com/user-attachments/assets/e64ef7c0-6513-4e55-baca-0ac713af1cd0" />

Precedência: Segue a matemática padrão (Potências $\rightarrow$ Mult/Div/Mód $\rightarrow$ Soma/Subtração).

## 3. Estruturas de Controle (Tomada de Decisão)

Essenciais para o fluxo de execução do programa.

### Operadores de Comparação:

<img width="295" height="243" alt="image" src="https://github.com/user-attachments/assets/4ac23dff-fb96-4a8f-83a5-2739a18a796a" />

### Estruturas Condicionais em Python (if, elif, else):

idade = 18

if idade >= 18:  
    print("Pode tirar a carteira de motorista.")  
elif idade >= 16:  
    print("Pode votar, mas não dirigir.")  
else:  
    print("É menor de idade.")  




