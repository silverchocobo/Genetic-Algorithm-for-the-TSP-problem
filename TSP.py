import pandas as pd
import numpy as np
from google.colab import drive


#Lê e converte linhas dos arquivos em dicionários através da biblioteca pandas
berlin52_df = pd.read_csv("../TSP_instances/berlin52.txt", sep=" ", header=None, names=["id", "x", "y"], on_bad_lines='skip')
berlin52_dict = berlin52_df.set_index("id").to_dict(orient="index")

eil51_df = pd.read_csv("../TSP_instances/eil51.txt", sep=" ", header=None, names=["id", "x", "y"], on_bad_lines='skip')
eil51_dict = eil51_df.set_index("id").to_dict(orient="index")

pr152_df = pd.read_csv("../TSP_instances/pr152.txt", sep=" ", header=None, names=["id", "x", "y"], on_bad_lines='skip')
pr152_dict = pr152_df.set_index("id").to_dict(orient="index")

rat99_df = pd.read_csv("../TSP_instances/rat99.txt", sep=" ", header=None, names=["id", "x", "y"], on_bad_lines='skip')
rat99_dict = rat99_df.set_index("id").to_dict(orient="index")

#Exibição dos dicinários

print(berlin52_dict)
print(eil51_dict)
print(pr152_dict)
print(rat99_dict)

"""

```
# Isto está formatado como código
```

#Criação da matriz de distâncias
Criaremos uma matriz de distâncias com a dimensão equivalente ao número total de cidades da instância. Também, declaramos a função para calcular a distância euclidiana entre duas cidades, que será usada na classe que calcula a aptidão da solução.
"""

# Criar a matriz de distâncias de Berlin
num_cities = len(berlin52_dict)
distance_matrix = np.zeros((num_cities, num_cities))
city_ids = list(berlin52_dict.keys())

#Valores possíveis
possible_values = num_cities

# Função para calcular a distância Euclidiana entre duas cidades
def euclidean_distance(city1, city2):
    return np.sqrt((city1["x"] - city2["x"])**2 + (city1["y"] - city2["y"])**2)

"""#Cálculo da aptidão

Criaremos a classe EvaluationRoads, que percorrerá a matriz de cidades e aplicará o cálculo da distância eucludiana entre as coordenadas entre os elementos, com o objetivo de calcular a aptidão (fitness) da solução.
"""

class EvaluationRoads:
  # armazena instância do problema na inicialização
    def __init__(self, n):
        self.n = n
  #Calcula valor da solução:
    def __call__(self, solution):
      total_distance = 0;

      for i in range(num_cities):
        for j in range(num_cities):
          if i != j:
            distance_matrix[i, j] = euclidean_distance(berlin52_dict[city_ids[i]], berlin52_dict[city_ids[j]])
            total_distance += distance_matrix[i, j]

      return total_distance

"""Considerando que a função objetivo avalia a qualidade (aptidão) de uma solução, para calcular a distância total do percurso, se utiliza a mesma função mencionada anteriormente:
![image-removebg-preview (2).png](data:image/png;base64,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)




Algoritimo do Vizinho mais Proximo
"""

# Algoritmo do Vizinho Mais Próximo (NN)
def nearest_neighbor_tsp(distance_matrix):
    num_cities = len(distance_matrix)
    visited = [False] * num_cities
    tour = [0]  # Começamos pela primeira cidade (índice 0)
    visited[0] = True
    total_distance = 0

    for _ in range(num_cities - 1):
        last_city = tour[-1]
        nearest_city = None
        min_distance = float("inf")

        for i in range(num_cities):
            if not visited[i] and distance_matrix[last_city, i] < min_distance:
                min_distance = distance_matrix[last_city, i]
                nearest_city = i

        tour.append(nearest_city)
        visited[nearest_city] = True
        total_distance += min_distance

    # Retorna à cidade inicial
    total_distance += distance_matrix[tour[-1], tour[0]]
    tour.append(tour[0])

    return tour, total_distance

# Executar o algoritmo NN para Berlin52
tour, total_distance = nearest_neighbor_tsp(distance_matrix)

# Exibir o resultado
print("Ordem das cidades visitadas:", [city_ids[i] for i in tour])
print("Distância total do percurso:", total_distance)

"""# Aplicação do Algoritimo Genético

Tendo como exemplo as instancias de "berlin52"


Declaração das Instancias:

Estado de Seleção por roleta:
"""

def select_tournament(pop_size, population, fitness_fn, k=3):
    selected = []
    for _ in range(pop_size):
        # Seleciona k indivíduos aleatoriamente da população
        tournament = random.sample(population, k)
        # Seleciona o indivíduo com o melhor fitness do torneio
        best_individual = max(tournament, key=fitness_fn)  # Buscando MAX, já que quanto menor o denominador, maior o retorno da fitness
        selected.append(best_individual)
    return selected

"""Estado de Cruzamento:"""

def order_crossover(parent1, parent2,num_cities):
    # Garante que só existam 10 genes (sem cidade duplicada no final)
    if parent1[0] == parent1[-1]:
        parent1 = parent1[:-1]
    if parent2[0] == parent2[-1]:
        parent2 = parent2[:-1]

    n = num_cities + 1  # Tamanho fixo de genes para evitar index out of range
    a, b = sorted(random.sample(range(n), 2))
    child = [None] * n

    # Copia fatia do primeiro pai
    child[a:b] = parent1[a:b]

    # Preenche os espaços vazios com genes do segundo pai
    p2_genes = [gene for gene in parent2 if gene not in child]

    idx = 0
    for i in range(n-1):
        if child[i] is None:
            child[i] = p2_genes[idx]
            idx += 1

    # Retorna à cidade inicial no final
    child = [gene for gene in child if gene is not None]

    child.append(child[0])
    return child

"""Estado de Mutação"""

def mutate_inversion(individual, pmut):
    if random.random() < pmut:
        i, j = sorted(random.sample(range(len(individual)), 2))
        individual[i:j] = reversed(individual[i:j])
    return individual

"""Aplicação:

#Instância Berlin52
"""

import random
import math
import bisect
import pandas as pd

#Declaração de Instancias


berlin52_df = pd.read_csv("berlin52.txt", sep=" ", header=None, names=["id", "x", "y"], on_bad_lines='skip')
berlin52_dict = berlin52_df.set_index("id").to_dict(orient="index")

#Função para calcular distância euclidiana entre cidades
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

#Função para calcular distância total de um caminho
def total_distance(route):
    return sum(
        dist(
            (berlin52_dict[route[i]]['x'], berlin52_dict[route[i]]['y']),
            (berlin52_dict[route[i+1]]['x'], berlin52_dict[route[i+1]]['y'])
        )
        for i in range(len(route)-1)
    ) + dist(
        (berlin52_dict[route[-1]]['x'], berlin52_dict[route[-1]]['y']),
        (berlin52_dict[route[0]]['x'], berlin52_dict[route[0]]['y'])
    )

#Função de fitness: quanto menor a distância, maior o fitness
def fitness(route):
    return 1 / (total_distance(route))

#Gerar população inicial
def init_population(size, city_ids):
    return [random.sample(city_ids, len(city_ids)) for _ in range(size)]

#Parâmetros
POP_SIZE = 1000
GENERATIONS = 500
PMUT = 0.1
city_ids = list(berlin52_dict.keys())
NUM_CITIES = len(city_ids)
population = init_population(POP_SIZE, city_ids)


#Loop evolutivo
for generation in range(GENERATIONS):
    # Seleção (torneio)
    selected = select_tournament(POP_SIZE, population, fitness)

    # Cruzamento (ponto único)
    offspring = []
    for i in range(0, POP_SIZE, 2):
        p1, p2 = selected[i], selected[i+1]
        child1 = order_crossover(p1, p2,NUM_CITIES)
        child2 = order_crossover(p2, p1, NUM_CITIES)

        offspring.extend([child1, child2])

    # Mutação (uniforme)
    gene_pool = city_ids.copy()

    mutated = [mutate_inversion(ind, PMUT) for ind in offspring]

    # Substituição direta
    population = mutated

#Melhor indivíduo final

#elitismo
elite = min(population, key=total_distance)
population[0] = elite  # substitui o primeiro pela elite
best = population[0]

print("Melhor rota:", best)
print("Distância:", total_distance(best))

"""#Instância Eil51"""

#Declaração de Instancias


eil51_df = pd.read_csv("eil51.txt", sep=" ", header=None, names=["id", "x", "y"], on_bad_lines='skip')
eil51_dict = eil51_df.set_index("id").to_dict(orient="index")

#Função para calcular distância euclidiana entre cidades
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

#Função para calcular distância total de um caminho
def total_distance(route):
    return sum(
        dist(
            (eil51_dict[route[i]]['x'], eil51_dict[route[i]]['y']),
            (eil51_dict[route[i+1]]['x'], eil51_dict[route[i+1]]['y'])
        )
        for i in range(len(route)-1)
    ) + dist(
        (eil51_dict[route[-1]]['x'], eil51_dict[route[-1]]['y']),
        (eil51_dict[route[0]]['x'], eil51_dict[route[0]]['y'])
    )

#Função de fitness: quanto menor a distância, maior o fitness
def fitness(route):
    return 1 / (total_distance(route))

#Gerar população inicial
def init_population(size, city_ids):
    return [random.sample(city_ids, len(city_ids)) for _ in range(size)]

#Parâmetros
POP_SIZE = 1000
GENERATIONS = 500
PMUT = 0.1
city_ids = list(eil51_dict.keys())
NUM_CITIES = len(city_ids)
population = init_population(POP_SIZE, city_ids)


#Loop evolutivo
for generation in range(GENERATIONS):
    # Seleção (torneio)
    selected = select_tournament(POP_SIZE, population, fitness)

    # Cruzamento (ponto único)
    offspring = []
    for i in range(0, POP_SIZE, 2):
        p1, p2 = selected[i], selected[i+1]
        child1 = order_crossover(p1, p2,NUM_CITIES)
        child2 = order_crossover(p2, p1, NUM_CITIES)

        offspring.extend([child1, child2])

    # Mutação (uniforme)
    gene_pool = city_ids.copy()

    mutated = [mutate_inversion(ind, PMUT) for ind in offspring]

    # Substituição direta
    population = mutated

#Melhor indivíduo final

#elitismo
elite = min(population, key=total_distance)
population[0] = elite  # substitui o primeiro pela elite
best = population[0]

print("Melhor rota:", best)
print("Distância:", total_distance(best))

"""#Instância Pr152"""

#Declaração de Instancias


pr152_df = pd.read_csv("pr152.txt", sep=" ", header=None, names=["id", "x", "y"], on_bad_lines='skip')
pr152_dict = pr152_df.set_index("id").to_dict(orient="index")

#Função para calcular distância euclidiana entre cidades
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

#Função para calcular distância total de um caminho
def total_distance(route):
    return sum(
        dist(
            (pr152_dict[route[i]]['x'], pr152_dict[route[i]]['y']),
            (pr152_dict[route[i+1]]['x'], pr152_dict[route[i+1]]['y'])
        )
        for i in range(len(route)-1)
    ) + dist(
        (pr152_dict[route[-1]]['x'], pr152_dict[route[-1]]['y']),
        (pr152_dict[route[0]]['x'], pr152_dict[route[0]]['y'])
    )

#Função de fitness: quanto menor a distância, maior o fitness
def fitness(route):
    return 1 / (total_distance(route))

#Gerar população inicial
def init_population(size, city_ids):
    return [random.sample(city_ids, len(city_ids)) for _ in range(size)]

#Parâmetros
POP_SIZE = 1000
GENERATIONS = 500
PMUT = 0.1
city_ids = list(pr152_dict.keys())
NUM_CITIES = len(city_ids)
population = init_population(POP_SIZE, city_ids)


#Loop evolutivo
for generation in range(GENERATIONS):
    # Seleção (torneio)
    selected = select_tournament(POP_SIZE, population, fitness)

    # Cruzamento (ponto único)
    offspring = []
    for i in range(0, POP_SIZE, 2):
        p1, p2 = selected[i], selected[i+1]
        child1 = order_crossover(p1, p2,NUM_CITIES)
        child2 = order_crossover(p2, p1, NUM_CITIES)

        offspring.extend([child1, child2])

    # Mutação (uniforme)
    gene_pool = city_ids.copy()

    mutated = [mutate_inversion(ind, PMUT) for ind in offspring]

    # Substituição direta
    population = mutated

#Melhor indivíduo final

#elitismo
elite = min(population, key=total_distance)
population[0] = elite  # substitui o primeiro pela elite
best = population[0]

print("Melhor rota:", best)
print("Distância:", total_distance(best))

"""#Instância Rat99"""

#Declaração de Instancias


rat99_df = pd.read_csv("rat99.txt", sep=" ", header=None, names=["id", "x", "y"], on_bad_lines='skip')
rat99_dict = rat99_df.set_index("id").to_dict(orient="index")

#Função para calcular distância euclidiana entre cidades
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

#Função para calcular distância total de um caminho
def total_distance(route):
    return sum(
        dist(
            (rat99_dict[route[i]]['x'], rat99_dict[route[i]]['y']),
            (rat99_dict[route[i+1]]['x'], rat99_dict[route[i+1]]['y'])
        )
        for i in range(len(route)-1)
    ) + dist(
        (rat99_dict[route[-1]]['x'], rat99_dict[route[-1]]['y']),
        (rat99_dict[route[0]]['x'], rat99_dict[route[0]]['y'])
    )

#Função de fitness: quanto menor a distância, maior o fitness
def fitness(route):
    return 1 / (total_distance(route))

#Gerar população inicial
def init_population(size, city_ids):
    return [random.sample(city_ids, len(city_ids)) for _ in range(size)]

#Parâmetros
POP_SIZE = 1000
GENERATIONS = 500
PMUT = 0.1
city_ids = list(rat99_dict.keys())
NUM_CITIES = len(city_ids)
population = init_population(POP_SIZE, city_ids)


#Loop evolutivo
for generation in range(GENERATIONS):
    # Seleção (torneio)
    selected = select_tournament(POP_SIZE, population, fitness)

    # Cruzamento (ponto único)
    offspring = []
    for i in range(0, POP_SIZE, 2):
        p1, p2 = selected[i], selected[i+1]
        child1 = order_crossover(p1, p2,NUM_CITIES)
        child2 = order_crossover(p2, p1, NUM_CITIES)

        offspring.extend([child1, child2])

    # Mutação (uniforme)
    gene_pool = city_ids.copy()

    mutated = [mutate_inversion(ind, PMUT) for ind in offspring]

    # Substituição direta
    population = mutated

#Melhor indivíduo final

#elitismo
elite = min(population, key=total_distance)
population[0] = elite  # substitui o primeiro pela elite
best = population[0]

print("Melhor rota:", best)
print("Distância:", total_distance(best))
