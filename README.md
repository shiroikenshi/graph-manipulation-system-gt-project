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
