# Traveling Salesman Problem

The Traveling Salesman Problem (TSP) is a well-known problem that simulates the route of a merchant traveling through several cities before returning to the city of origin.

The problem requires us to calculate the best route to visit a list of cities from a given instance. To do this, we will create a dictionary for each instance of the problem, containing the index of the list and the x and y coordinates.

## Problem Analysis

TSP is fully observable, sequential, single-agent, deterministic, static, discrete, and known. It has a large number of possible solutions, and to find the best one, we will use a genetic algorithm, whose abstraction can be represented by the pseudocode below (RUSSELL; NORVIG, 2022, p. 106):

```
function GENETIC-ALGORITHM(population, fitness) returns an individual
repeat
  weights ← WEIGH-BY(population, fitness)
  new_population ← empty list
  for i = 1 to SIZE(population) do
    parent1, parent2 ← RANDOM-SELECTION(population, weights, 2)
    child ← REPRODUCE(parent1, parent2)
    if (small random probability) then child ← MUTATE(child)
    add child to new_population
  population ← new_population
until an individual is fit enough or enough time has passed
return the best individual in population, according to fitness
```

## Mathematical Statement of the Problem
Considering that it is a combinatorial optimization problem that seeks to find the shortest route that visits all the cities in a given set:

![Captura de tela 2025-04-21 014539](https://github.com/user-attachments/assets/302ad6e3-20d5-4abd-b14f-e727d34a30be)

## Mathematical Formulation of the Problem

**π**: A permutation of the cities, i.e., a visiting order. For example, if we have 4 cities, π = (2, 3, 1, 4) indicates that the visiting order will be city 2 → 3 → 1 → 4.

**dᵢⱼ**: The distance between cities i and j.

**∑ⁿ⁻¹ᵢ₌₁ d₍π(i),π(i+1)₎**: Sums the distances between each city and the next one in the permutation, except for the return to the starting point.

**π(i)**: The city at position i in the permutation.

**d₍π(n),π(1)₎**: Adds the distance from the last city back to the first, forming a closed loop.

Example: If we have 4 cities in a set (1, 3, 4, 2)
The path will be: 1 → 3 → 4 → 2
And the total cost will be: d₁,₃ + d₃,₄ + d₄,₂ + d₂,₁

## Search Space

The search space is the set of all possible permutations of n cities, that is:

**|S| = n!**

Using the example of the instance "Berlin52", we have a search space of 52!, which results in approximately 8.07 × 10⁶⁷.

The size of such a search space is the reason why exact techniques become impractical, and heuristic methods are recommended.

## Solution Encoding

Each individual in the population represents a possible solution to the problem — that is, a permutation of the cities.

Formally, an individual is a vector π = [π₁, π₂, π₃, ..., πₙ], where πᵢ ∈ {1, 2, ..., n} and all πᵢ are distinct.
