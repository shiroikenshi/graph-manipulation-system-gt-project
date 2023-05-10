# <div align="center"><a href="/README.md">Português</a> | <a href="/README_EN.md">Inglês</a></div>
<br><br>
# Teoria dos Grafos - Sistema de Manipulação de Grafos
Este repositório contém um sistema de manipulação de grafos implementado em Python. O sistema permite a criação de um grafo, adição de vértices e arestas, cálculo do grau mínimo e máximo, criação da matriz de adjacência, busca em largura, busca em profundidade e identificação dos componentes conexos do grafo.

### Autores
* Felipe Pinto da Silva | RGM: 26533952
* Catherine Ferreira Honorato | RGM: 25971573
* Camila Ferreira de Sousa | RGM: 28396073
* Hugo Nascimento Pedro | RGM: 26370174

### Funcionalidades
#### Classe Grafo
A classe Grafo representa um grafo e possui os seguintes métodos:

* __init__(): Inicializa um objeto Grafo vazio.
* adicionar_vertice(vertice): Adiciona um vértice ao grafo.
* adicionar_aresta(vertice1, vertice2): Adiciona uma aresta entre dois vértices do grafo.
* calcular_grau_minimo(): Calcula e retorna o grau mínimo do grafo.
* calcular_grau_maximo(): Calcula e retorna o grau máximo do grafo.
* criar_matriz_adjacencia(): Cria e retorna a matriz de adjacência do grafo.
* busca_largura(vertice_inicial): Aplica a busca em largura no grafo a partir de um vértice inicial e retorna a ordem de visita dos vértices.
* busca_profundidade(vertice_inicial): Aplica a busca em profundidade no grafo a partir de um vértice inicial e retorna a ordem de visita dos vértices.
* componentes_conexos(): Encontra e retorna os componentes conexos do grafo.

#### Funções de Apoio
* ler_arquivo(nome_arquivo): Lê um arquivo contendo a descrição do grafo e retorna a matriz de adjacência e um objeto Grafo.
* escrever_arquivo(nome_arquivo, linhas): Escreve os resultados das buscas e dos componentes conexos em um arquivo de texto.

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
12. Informações sobre os componentes do grafo serão exibidas.

### Exemplo de aplicação do código
#### 1. Descrição do grafo:
Suponha que temos a descrição do grafo assim como na primeira imagem abaixo no arquivo grafo.txt:

![image](https://github.com/shiroikenshi/graph-manipulation-system/assets/131435772/1d83eef9-2d81-4727-a706-630e5e07c5c6)

Nesse caso, temos um grafo com 4 vértices (representados pela primeira linha) e 4 arestas (representados pela linhas posteriores). Nesse exemplo nossas arestas são as seguintes: (1,2), (2,3), (1,4) e (2,4).
#### 2. Execução do código:
Após configurar o arquivo grafo.txt corretamente rode o sistema.

#### 3. Resultados iniciais:
O sistema exibirá as seguintes informações sobre o grafo:
* Número de vértices: 4
* Número de arestas: 4
* Grau mínimo: 1
* Grau máximo: 2

* Matriz de Adjacência:<br>
[0, 1, 0, 1]<br>
[1, 0, 1, 1]<br>
[0, 1, 0, 0]<br>
[1, 1, 0, 0]

#### 4. Busca em largura e profundidade:
O sistema solicitará um vértice inicial para realizar as buscas em largura e em profundidade. Nesse exemplo escolheremos o vértice 1 como inicial.

#### 5. Componentes conexos:
O sistema identificará os componentes conexos do grafo, ou seja, grupos de vértices que estão interligados entre si.

#### 6. Resultados finais:
O sistema exibirá as seguintes informações:
* Busca em Largura: [1, 2, 4, 3]
* Busca em Profundidade: [1, 2, 3, 4]

* Qtd. Componentes conexos: 1<br>
Componente 1: {1, 2, 4, 3}

#### 7. Escrevendo resultados em arquivos de texto:
Finalizando o sistema irá criar e escrever os resultados obtidos pelas buscas (largura e profundidade) e verificação de componentes em dois arquivos de texto. Respectivamente "buscas.txt" e "componentes.txt".
