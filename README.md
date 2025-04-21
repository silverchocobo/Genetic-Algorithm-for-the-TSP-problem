# Traveling Salesman Problem

The Traveling Salesman Problem (TSP) is a well-known problem that simulates the route of a merchant traveling through several cities before returning to the city of origin.

The problem requires us to calculate the best route to visit a list of cities from a given instance. To do this, we will create a dictionary for each instance of the problem, containing the index of the list and the x and y coordinates.

## Problem Analysis

TSP is fully observable, sequential, single-agent, deterministic, static, discrete, and known. It has a large number of possible solutions, and to find the best one, we will use a genetic algorithm, whose abstraction can be represented by the pseudocode below (RUSSELL; NORVIG, 2022, p. 106):

'''
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
'''
