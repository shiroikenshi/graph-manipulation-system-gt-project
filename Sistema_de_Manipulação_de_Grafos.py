# Teoria dos Grafos - Sistema de Manipulação de Grafos

# Autores: Felipe Pinto da Silva | RGM: 26533952
#          Catherine Ferreira Honorato | RGM: 25971573
#          Camila Ferreira de Sousa | RGM: 28396073
#          Hugo Nascimento Pedro | RGM: 26370174

# Define a classe Grafo que será usada para representar um Grafo
class Grafo:
    # Define um objeto Grafo como vazio
    def __init__(self):
        # Dicionário para armazenar os vértices do Grafo
        self.vertices = {}
        # Número de vértices do Grafo
        self.num_vertices = 0
        # Número de arestas do Grafo
        self.num_arestas = 0
    
    # Adiciona um vértice ao Grafo
    def adicionar_vertice(self, vertice):
        # Verifica se o vertice já existe no dicionário de vértices
        if vertice not in self.vertices:
            # Adiciona o vértice no dicionário
            self.vertices[vertice] = []
            # Incrementa o contador de vértices
            self.num_vertices += 1
    
    # Adiciona uma aresta entre dois vértices no Grafo
    def adicionar_aresta(self, vertice1, vertice2):
        # Verifica se ambos os vértices estão presentes no dicionário
        if vertice1 in self.vertices and vertice2 in self.vertices:
            # Adiciona a aresta através das duas próximas linhas de código
            # Adiciona vertice2 à lista de vértices adjacentes de vértice1
            self.vertices[vertice1].append(vertice2)
            # Adiciona vertice1 à lista de vértices adjacentes de vértice2
            self.vertices[vertice2].append(vertice1)
            # Incrementa o contador de arestas
            self.num_arestas += 1
    
    # Calcula e retorna o grau mínimo do Grafo
    def calcular_grau_minimo(self):
        # Atribui um referencial inicial infinito ao grau mínimo
        grau_minimo = float('inf')
        # Percorre todos os vértices no dicionário de vértices do Grafo
        for vertice in self.vertices:
            # Calcula o grau de cada vértice
            # self.vertices[vertice] retorna a lista de vértices adjacentes ao vértice atual
            # len(set(...)) retorna o número de elementos distintos nessa lista
            grau_vertice = len(set(self.vertices[vertice]))
            # Verifica se o grau_vertice é menor que grau_minimo
            if grau_vertice < grau_minimo:
                # Atualiza o valor de grau_minimo com grau_vertice
                grau_minimo = grau_vertice
        # Retorna grau_minimo
        return grau_minimo

    # Calcula e retorna o grau máximo
    def calcular_grau_maximo(self):
        # Atribui zero ao grau máximo
        grau_maximo = 0
        # Percorre todos os vértices no dicionário de vértices do Grafo
        for vertice in self.vertices:
            # Calcula o grau de cada vértice (detalhes na função anterios)
            grau_vertice = len(set(self.vertices[vertice]))
            # Verifica se o grau_vertice é maior que grau_maximo
            if grau_vertice > grau_maximo:
                # Atualiza o valor de grau_maximo com grau_vertice
                grau_maximo = grau_vertice
        # Retorna grau_maximo
        return grau_maximo
    
    # Cria e retorna a matriz de adjacência do Grafo
    def criar_matriz_adjacencia(self):
        # Cria uma matriz preenchida com zeros, com dimensões self.num_vertices x self.num_vertices
        matriz_adjacencia = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        # Percorre todos os vértices no dicionário de vértices do Grafo
        for vertice in self.vertices:
            # Percorre todos os vértices adjacentes ao vértice atual
            for adjacente in self.vertices[vertice]:
                # Define o valor 1 na matriz de adjacência para indicar que os vertices são adjacentes
                matriz_adjacencia[vertice-1][adjacente-1] = 1
        # Retorna matriz_adjacencia
        return matriz_adjacencia
    
    # Aplica e retorna a busca em largura em um Grafo, recebe o vértice inicial como parâmetro
    def busca_largura(self, vertice_inicial):
        # Crua um objeto do tipo set e atribui ele a variável visitados
        # O objeto set não permite valores duplicados, portanto será útil na nossa função
        visitados = set()
        # Fila para controlar a ordem de visita dos vértices, recebe vertice_inicial inicialmente
        fila = [vertice_inicial]
        # Lista que armazenará a ordem em que os vértices foram visitados
        ordem_visita = []
        # Loop while será executado enquanto a lista não estiver vazia
        while fila:
            # O primeiro vértice da fila é removido e atribuido à variável vertice_atual
            vertice_atual = fila.pop(0)
            # Verifica se vertice_atual ainda não foi visitado
            if vertice_atual not in visitados:
                # Adiciona vertice_atual ao conjunto dos visitados
                visitados.add(vertice_atual)
                # Adiciona vertice_atual a lista ordem_visita
                ordem_visita.append(vertice_atual)
                # Percorre todos os vértices adjacentes a vertice_atual
                for adjacente in self.vertices[vertice_atual]:
                    # Verifica se o vértice adjacente ainda não foi visitado
                    if adjacente not in visitados:
                        # Adiciona o vértice à fila para ser visitado posteriormente
                        fila.append(adjacente)
        # Retorna lista de ordem_visita
        return ordem_visita
    
    # Aplica e retorna a busca em profundidade em um Grafo, recebe o vértice inicial como parâmetro
    def busca_profundidade(self, vertice_inicial):
        # Cria um objeto do tipo set e atribui ele a variável visitados, explicação na função busca_largura
        visitados = set()
        # Lista que armazenará a ordem em que os vértices foram visitados
        ordem_visita = []
        # Define uma função auxiliar que realiza a busca em profundidade de forma recursiva
        # Ela é definida dentro de busca_profundidade para ter acesso ao conjunto visitados e a lista ordem_visita
        def dfs(vertice):
            # Adiciona o vértice atual ao conjunto dos visitados
            visitados.add(vertice)
            # Adiciona o vertice atual a lista ordem_visita
            ordem_visita.append(vertice)
            # Percorre todos os vértices adjacentes ao vértice atual
            for adjacente in self.vertices[vertice]:
                # Verifica se o vértice adjacente ainda não foi visitado
                if adjacente not in visitados:
                    # Chama recursivamente a função dfs para visitar o vértice adjacente
                    dfs(adjacente)
        # Inicia a busca em profundidade chamando a função dfs com vertice_inicial como parâmetro
        dfs(vertice_inicial)
        # Retorna lista de ordem_visita
        return ordem_visita
    
    # Encontra os componentes conexos em um Grafo
    def componentes_conexos(self):
        # Cria um objeto do tipo set e atribui ele a variável visitados, explicação na função busca_largura
        visitados = set()
        # Cria uma lista para armazenar os componentes conexos encontrados
        componentes = []
        # Percorre todos os vértices no dicionário de vértices do Grafo
        for vertice in self.vertices:
            # Verifica se o vértice atual ainda não foi visitado
            if vertice not in visitados:
                # Chama a função busca_largura para obter o componente conexo do vértice atual
                componente_atual = self.busca_largura(vertice)
                # Adiciona os vértices visitados pelo componente atual ao conjunto visitados
                visitados.update(componente_atual)
                # Adiciona o componente atual a lista de componentes
                componentes.append(componente_atual)
        # Retorna lista de componentes
        return componentes

# Função para ler o arquivo Grafo.txt
def ler_arquivo(nome_arquivo):
    # Cria uma instância da classe Grafo
    grafo = Grafo()
    # Abre o arquivo especificado em modo leitura "r"
    # O uso do with garante que o arquivo será fechado corretamente ao final do bloco
    with open(nome_arquivo, 'r') as arquivo:
        # Lê todas as linhas do arquivo e armazena em uma lista chamada linhas
        linhas = arquivo.readlines()
        # Obtém a quantidade de vértices do Grafo a partir da primeira linha do arquivo
        quantidade_vertices = int(linhas[0])
        # Percorre quantidade_vertices até quantidade_vertices + 1
        for i in range(1, quantidade_vertices+1):
            # Adiciona um vértice ao Grafo
            grafo.adicionar_vertice(i)
        # Percorre cada linha da lista linhas, a partir da segunda linha até o final
        for linha in linhas[1:]:
            # linha.split() Quebra a string linha em substrings nos espaços em branco, retornando uma lista contendo as substrings resultantes
            # map(int, ...) Converte cada substring em um número inteiro
            # list(...) Cria uma lista a partir dos elementos de map()
            # Por fim atribui a lista à variável vertices
            vertices = list(map(int, linha.split()))
            # Obtem o primeiro vértice da lista de vértices
            vertice1 = vertices[0]
            # Obtem o segundo vértice da lista de vértices
            vertice2 = vertices[1]
            # Adiciona uma aresta entre os vértices
            grafo.adicionar_aresta(vertice1, vertice2)
    # Chama o método criar_matriz_adjacencia para criar a matriz de adjacência do Grafo
    matriz_adjacencia = grafo.criar_matriz_adjacencia()
    # Retorna matriz_adjacencia, num_vertices e num_arestas do Grafo
    return matriz_adjacencia, grafo

# Função responsável por escrever os resultados obtidos nas buscas e componentes em arquivos .txt
def escrever_arquivo(nome_arquivo, linhas):
    # Abre o arquivo especificado no modo escrita "w"
    # O uso do with foi explicado na função ler_arquivo
    with open(nome_arquivo, 'w') as arquivo:
        # Escreve uma sequência de strings de linhas nos arquivo .txt
        arquivo.writelines(linhas)

# Lê o arquivo grafo.txt chamando a função ler_arquivo, retorna dois valores respectivos para matriz_adjacencia, Grafo
matriz_adjacencia, grafo = ler_arquivo('grafo.txt')

# Específica para o usuário o arquivo txt contendo o grafo que será utilizado pelo sistema
print("\nManipulação sendo realizada com o grafo presente no arquivo grafo.txt")

# Imprime número de vértices do Grafo
print(f"\na. Número de vértices: {grafo.num_vertices}")
# Imprime número de arestas do Grafo
print(f"b. Número de arestas: {grafo.num_arestas}")
# Imprime grau minimo do Grafo
print(f"c. Grau mínimo: {grafo.calcular_grau_minimo()}")
# Imprime grau máximo do Grafo
print(f"d. Grau máximo: {grafo.calcular_grau_maximo()}")

# Exibindo Matriz de Adjacência
print("\ne. Matriz de Adjacência:")
# Percorre cada linha de matriz_adjacencia
for linha in matriz_adjacencia:
    # Printa cada linha de matriz_adjacencia
    print(linha)

# While True para solicitar ao usuário um vértice inicial para realizar as buscas
while True:
    # Solicita para o usuário e armazena o vértice em vertice_inicial
    vertice_inicial = int(input("\nf. Digite o vértice inicial para as buscas (Largura e Profundidade): "))
    # Verifica se o vértice informado existe nos vértices
    if vertice_inicial in grafo.vertices:
        # Escerra o loop
        break
    # Condição caso o vértice informado não exista nos vértices
    else:
        # Imprime uma mensagem de erro para o usuário
        print("Vértice inválido. Por favor, digite um vértice válido!")

# Realiza a busca em largura no Grafo com a função busca_largura
ordem_visita_largura = grafo.busca_largura(vertice_inicial)
# Imprime a ordem de visita dos vértices resultante da busca em largura
print(f"Busca em Largura: {ordem_visita_largura}")

# Realiza a busca em profundidade no Grafo com a função busca_profundidade
ordem_visita_profundidade = grafo.busca_profundidade(vertice_inicial)
# Imprime a ordem de visita dos vértices resultante da busca em profundidade
print(f"Busca em Profundidade: {ordem_visita_profundidade}\n")

# Realiza a contagem dos componentes conexos do Grafo com a função componentes_conexos
componentes = grafo.componentes_conexos()
# Imprime a quantidade de componentes conexos presentes no Grafo
print(f"g. Qtd. Componentes conexos: {len(componentes)}")
# Percorre componentes
for i, componente in enumerate(componentes):
    # Imprime cada componente percorrido
    print(f"Componente {i + 1}: {componente}")

# Define um nome de arquivo.txt para armazenar os resultados das buscas (largura e profundidade)
buscas_nome_arquivo = 'buscas.txt'
# Define um nome de arquivo.txt para armazenar os resultados dos componentes conexos
componentes_nome_arquivo = 'componentes.txt'

# Cria uma linha contendo as linhas que serão escritas no arquivo buscas.txt
buscas_linhas = [
    # Cria a primeira linha, que receberá a ordem da visita da busca em largura no Grafo
    f"Busca em Largura: {ordem_visita_largura}\n",
    # Cria a segunda linha, que receberá a ordem da visita da busca em profundidade no Grafo
    f"Busca em Profundidade: {ordem_visita_profundidade}"
]
# Cria uma linha contendo as linhas que serão escritas no arquivo componentes.txt
componentes_linhas = [
    # Cria a primeira linha, que exibirá a quantidade de componentes conexos no Grafo
    f"Qtd. Componentes conexos: {len(componentes)}\n"
]
# Adiciona mais várias linhas a componentes_linhas para representar os componentes conexos
componentes_linhas.extend([
    # f"Componente {i + 1} Indica o número do componente
    # {', '.join(str(vertice) for vertice in componente)} Cria uma string com todos os vértices do componente e os converte
    # {', '.join(...(...))...)} Junta todas as strings dos vértices usando vírgula e espaço
    f"Componente {i + 1}: {{{', '.join(str(vertice) for vertice in componente)}}}\n" for i, componente in enumerate(componentes)
])

# Chama a função escrever_arquivo para escrever buscas_linhas no arquivo buscas.txt
escrever_arquivo(buscas_nome_arquivo, buscas_linhas)
# Chama a função escrever_arquivo para escrever componentes_linhas no arquivo componentes.txt
escrever_arquivo(componentes_nome_arquivo, componentes_linhas)

# Imprime uma mensagem para o usuário informando que os arquivos de texto foram gerados com sucesso
print("\nOs arquivos txt de buscas e componentes foram gerados dentro do diretório.\n")