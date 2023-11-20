# <div align="center"><a href="/README.md">Português</a> | <a href="/README_EN.md">Inglês</a></div>
<br><br>
# Teoria dos Grafos - Sistema de Manipulação de Grafos
Este repositório contém um sistema de manipulação de grafos implementado em Python. O sistema permite a criação de um grafo, adição de vértices e arestas, cálculo do grau mínimo e máximo, criação da matriz de adjacência, busca em largura, busca em profundidade e identificação dos componentes conexos do grafo.

### Autor
* Felipe Pinto da Silva

### Funcionalidades
#### Classe Grafo
A classe Grafo representa um grafo e possui os seguintes métodos:

* ```__init__()``` - Inicializa um objeto Grafo vazio.
* ```adicionar_vertice(vertice)``` - Adiciona um vértice ao grafo.
* ```adicionar_aresta(vertice1, vertice2)``` - Adiciona uma aresta entre dois vértices do grafo.
* ```calcular_grau_minimo()``` - Calcula e retorna o grau mínimo do grafo.
* ```calcular_grau_maximo()``` - Calcula e retorna o grau máximo do grafo.
* ```criar_matriz_adjacencia()``` - Cria e retorna a matriz de adjacência do grafo.
* ```busca_largura(vertice_inicial)``` - Aplica a busca em largura no grafo a partir de um vértice inicial e retorna a ordem de visita dos vértices.
* ```busca_profundidade(vertice_inicial)``` - Aplica a busca em profundidade no grafo a partir de um vértice inicial e retorna a ordem de visita dos vértices.
* ```componentes_conexos()``` - Encontra e retorna os componentes conexos do grafo.

#### Funções de Apoio
* ```ler_arquivo(nome_arquivo)``` - Lê um arquivo contendo a descrição do grafo e retorna a matriz de adjacência e um objeto Grafo.
* ```escrever_arquivo(nome_arquivo, linhas)``` - Escreve os resultados das buscas e dos componentes conexos em um arquivo de texto.

### Utilização
#### Utilizando uma IDE (Ambiente de Desenvolvimento Integrado):

1. Clone o repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado em seu computador.
3. Abra a sua IDE preferida (por exemplo, PyCharm, Visual Studio Code, Atom).
4. Abra a pasta do projeto na IDE.
5. Localize o arquivo Python que contém o código e abra-o.
6. Modifique o arquivo "grafo.txt" para definir a descrição do grafo, seguindo o formato fornecido.
7. Execute o código clicando no botão "Executar" ou "Play" na IDE.
8. O sistema lerá o arquivo "grafo.txt" para obter a descrição do grafo.
9. Informações sobre o grafo, como o número de vértices, número de arestas, grau mínimo e grau máximo, serão exibidas.
10. A matriz de adjacência do grafo será criada e exibida na tela.
11. Será solicitado ao usuário que informe um vértice inicial para realizar as buscas em largura e em profundidade.
12. Informações contendo o caminho resultante das buscas serão exibidas na tela.
13. Informações sobre os componentes do grafo serão exibidas.
14. Por fim, os arquivos .txt de saída para as buscas e componentes serão gerados.

### Exemplo de aplicação do código
#### 1. Descrição do grafo:
Suponha que temos a descrição abaixo do grafo dentro do arquivo grafo.txt:
```
4
1 2
1 4
2 3
2 4
```
Nesse caso, temos um grafo com 4 vértices (representados pela primeira linha) e 4 arestas (representados pela linhas posteriores). Nesse exemplo nossas arestas são as seguintes: (1,2), (1,4), (2,3) e (2,4). Para manter a correta representação das conexões no grafo, é importante manter a ordem dos vértices quando formos descrever cada aresta. Como no exemplo anterior.

#### 2. Execução do código:
Após configurar o arquivo grafo.txt corretamente rode o sistema.

#### 3. Resultados iniciais:
O sistema exibirá as seguintes informações sobre o grafo:
```
Manipulação sendo realizada com o grafo presente no arquivo grafo.txt

a. Número de vértices: 4
b. Número de arestas: 4
c. Grau mínimo: 1
d. Grau máximo: 2

e. Matriz de Adjacência:
[0, 1, 0, 1]
[1, 0, 1, 1]
[0, 1, 0, 0]
[1, 1, 0, 0]
```
#### 4. Busca em largura e profundidade:
O sistema solicitará um vértice inicial para realizar as buscas em largura e em profundidade. Nesse exemplo escolheremos o vértice 1 como inicial.
```
f. Digite o vértice inicial para as buscas (Largura e Profundidade): 1
```
#### 5. Componentes conexos:
O sistema identificará os componentes conexos do grafo, ou seja, grupos de vértices que estão interligados entre si.

#### 6. Resultados finais:
O sistema exibirá as seguintes informações:
```
Busca em Largura: [1, 2, 4, 3]
Busca em Profundidade: [1, 2, 3, 4]

g. Qtd. Componentes conexos: 1
Componente 1: {1, 2, 4, 3}
```
#### 7. Escrevendo resultados em arquivos de texto:
Finalizando o sistema irá criar e escrever os resultados obtidos pelas buscas (largura e profundidade) e verificação de componentes em dois arquivos de texto. Respectivamente "buscas.txt" e "componentes.txt". Irá imprimir na tela um texto informativo notificando o usuário que os arquivos de texto foram gerados dentro do diretório.
```
Os arquivos txt de buscas e componentes foram gerados dentro do diretório.
```
