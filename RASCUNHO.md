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

**Estruturas Condicionais** em Python (`if`, `elif`, `else`):

<img width="418" height="182" alt="image" src="https://github.com/user-attachments/assets/5bc89152-63d3-4185-844f-b7829248100b" />

### Operadores Lógicos (Combinação de Condições):

- and (E lógico): Só é True se ambas as condições forem True.
- or (OU lógico): É True se pelo menos uma condição for True.
- not (NÃO lógico): Inverte o valor lógico.

Exemplo:

<img width="705" height="118" alt="image" src="https://github.com/user-attachments/assets/858e47ff-deb4-4f82-8f2a-dd1a2e28b466" />


## 4. Estruturas de Repetição (Laços/Loops)
   
Usadas quando um bloco de código precisa ser executado várias vezes.

**A.** `for` **(Repetição com Contador Fixo)**

Ideal para percorrer uma sequência ou repetir um número exato de vezes.

#Imprime números de 0 a 4  
for i in range(5):  
    print(f"Contagem: {i}")

#Percorrendo elementos de uma lista
frutas = ["maçã", "banana", "uva"]  
for fruta in frutas:  
    print(f"Eu gosto de {fruta}")  

**B.** `while` **(Repetição com Condição)**

Ideal para repetir um bloco de código enquanto uma condição for verdadeira. Atenção: A condição deve se tornar falsa em algum momento para evitar loops infinitos.

contador = 0  
while contador < 3:  
   print(f"O contador é {contador}")  
   contador = contador + 1 # Incremento crucial para parar o loop  

print("Loop finalizado.")

## 5. Estruturas de Dados (Coleções)
   
Para organizar múltiplos dados de forma estruturada:

- **Lista** (`list`): Coleção **ordenada** e **mutável** (pode ser alterada).  
**Exemplo:** `minha_lista = [10, 20, 30, "a"]`

- Tupla (`tuple`): Coleção ordenada e imutável (não pode ser alterada após criada).  
**Exemplo:** `minha_tupla = (1, 2, 3)`

- **Dicionário** (`dict`): Coleção de pares **chave: valor**. Ótimo para mapeamentos.  
**Exemplo:** `pessoa = {"nome": "Ana", "idade": 25}`

## 6. Funções (Modularização)

Funções são blocos de código reutilizáveis. Elas ajudam a dividir um algoritmo grande em partes menores e gerenciáveis.

#Definição da função (usando a palavra-chave def)  
def calcular_quadrado(numero):  
    """Esta função calcula o quadrado de um número."""  
    resultado = numero ** 2  
    return resultado # Devolve o resultado para quem chamou  

#Chamada da função
valor = 5  
quadrado_de_5 = calcular_quadrado(valor)  

print(f"O quadrado de {valor} é {quadrado_de_5}")


# Conclusão: A Jornada do Algoritmo para o Código

Para dominar a lógica com Python, siga este ciclo:

1. **Entenda o Problema:** O que você quer que o programa faça?
2. **Desenhe o Algoritmo:** Esboce o passo a passo em Pseudocódigo ou Fluxograma.
3. **Traduza para Python:** Implemente as **Variáveis**, **Condicionais** (`if`/`else`) e Laços (`for`/`while`) definidos no seu algoritmo usando a sintaxe correta do Python.
4. **Teste e Refine:** Execute o código com diferentes entradas para garantir que a lógica está correta em todos os cenários.





