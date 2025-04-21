# Traveling Salesman Problem

The Traveling Salesman Problem (TSP) is a well-known problem that simulates the route of a merchant traveling through several cities before returning to the city of origin.

The Traveling Salesman Problem requires us to calculate the best route to visit a list of cities from a given instance. To do this, we will create a dictionary for each instance of the problem, containing the index of the list and the x and y coordinates.

## Problem Analysis

The Traveling Salesman Problem is fully observable, sequential, single-agent, deterministic, static, discrete, and known. It has a large number of possible solutions, and to find the best one, we will use a genetic algorithm, whose abstraction can be represented by the pseudocode below (RUSSELL; NORVIG, 2022, p. 106):
