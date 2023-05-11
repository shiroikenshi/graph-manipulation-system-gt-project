# <div align="center"><a href="/README.md">Portuguese</a> | <a href="/README_EN.md">English</a></div>
<br><br>
# Graph Theory - Graph Manipulation System
This repository contains a graph manipulation system implemented in Python. The system allows for graph creation, addition of vertices and edges, calculation of minimum and maximum degree, creation of adjacency matrix, breadth-first search, depth-first search, and identification of connected components in the graph.

### Authors
* Felipe Pinto da Silva | RGM: 26533952
* Catherine Ferreira Honorato | RGM: 25971573
* Camila Ferreira de Sousa | RGM: 28396073
* Hugo Nascimento Pedro | RGM: 26370174

### Features
#### Graph Class
The Graph class represents a graph and has the following methods:

* __init__(): Initializes an empty Graph object.
* adicionar_vertice(vertice): Adds a vertex to the graph.
* adicionar_aresta(vertice1, vertice2): Adds an edge between two vertices of the graph.
* calcular_grau_minimo(): Calculates and returns the minimum degree of the graph.
* calcular_grau_maximo(): Calculates and returns the maximum degree of the graph.
* criar_matriz_adjacencia(): Creates and returns the adjacency matrix of the graph.
* busca_largura(vertice_inicial): Applies breadth-first search on the graph starting from an initial vertex and returns the order of visited vertices.
* busca_profundidade(vertice_inicial): Applies depth-first search on the graph starting from an initial vertex and returns the order of visited vertices.
* componentes_conexos(): Finds and returns the connected components of the graph.

#### Support Functions
* ler_arquivo(nome_arquivo): Reads a file containing the graph description and returns the adjacency matrix and a Graph object.
* escrever_arquivo(nome_arquivo, linhas): Writes the results of breadth-first search, depth-first search, and connected components to a text file.

### Usage
#### Using an IDE (Integrated Development Environment):

1. Clone the repository to your local environment.
2. Make sure you have Python installed on your computer.
3. Open your preferred IDE (e.g., PyCharm, Visual Studio Code, Atom).
4. Open the project folder in the IDE.
5. Locate the Python file that contains the code and open it.
6. Modify the "graph.txt" file to define the graph description following the provided format.
7. Run the code by clicking the "Run" or "Play" button in the IDE.
8. The system will read the "graph.txt" file to obtain the graph description.
9. Information about the graph, such as the number of vertices, number of edges, minimum degree, and maximum degree, will be displayed.
10. The adjacency matrix of the graph will be created and displayed on the screen.
11. The user will be prompted to enter an initial vertex to perform breadth-first and depth-first searches.
12. Information about the graph's connected components will be displayed.

### Example of Code Application
#### 1. Graph Description:
Suppose we have the graph description as shown in the image below in the "grafo.txt" file:

![image](https://github.com/shiroikenshi/graph-manipulation-system/assets/131435772/1d83eef9-2d81-4727-a706-630e5e07c5c6)

In this case, we have a graph with 4 vertices (represented by the first line) and 4 edges (represented by the subsequent lines). In this example, our edges are: (1,2), (2,3), (1,4), and (2,4).
#### 2. Code Execution:
After properly configuring the "grafo.txt" file, run the system.

#### 3. Initial Results:
The system will display the following information about the graph:
```
Manipulation is being performed with the graph present in the file "grafo.txt"

a. Number of vertices: 4
b. Number of edges: 4
c. Minimum degree: 1
d. Maximum degree: 2

e. Adjacency Matrix:
[0, 1, 0, 1]
[1, 0, 1, 1]
[0, 1, 0, 0]
[1, 1, 0, 0]
```
#### 4. Breadth-First and Depth-First Search:
The system will prompt for an initial vertex to perform breadth-first and depth-first searches. In this example, we will choose vertex 1 as the initial vertex.
```
f. Enter the initial vertex for the searches (Breadth-first and Depth-first): 1
```
#### 5. Connected Components:
The system will identify the connected components of the graph, i.e., groups of vertices that are interconnected.

#### 6. Final Results:
The system will display the following information:
```
Breadth-First Search: [1, 2, 4, 3]
Depth-First Search: [1, 2, 3, 4]

g. Number of Connected Components: 1
Component 1: [1, 2, 4, 3]
```
#### 7. Writing Results to Text Files:
Upon completion, the system will create and write the results obtained from the breadth-first and depth-first searches, as well as the identification of components, to two text files named "searches.txt" and
"components.txt", respectively. It will print an informative text on the screen notifying the user that the text files have been generated inside the directory.
```
The search and component txt files were generated inside the directory.
```
