import random

import folium

from voyageur.glouton import transObjectList, listVilles, mapp
import random
from math import radians, sin, cos, sqrt, atan2

# Coordonnées GPS de l'objectif
objective_latitude = 48.8566  # Latitude de Paris
objective_longitude = 2.3522  # Longitude de Paris

# Définition de la distance entre deux points GPS (utilisation de la formule de haversine)
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon de la Terre en kilomètres

    # Conversion des degrés en radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Calcul des différences de latitude et de longitude
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Formule de Haversine pour calculer la distance
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

# Définition de la fonction d'évaluation d'un individu (distance entre le point et l'objectif)
def evaluate_individual(individual):
    latitude, longitude = individual
    return haversine_distance(latitude, longitude, objective_latitude, objective_longitude)

# Génération d'un individu aléatoire
def generate_individual():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return [latitude, longitude]

# Génération d'une population initiale
def generate_population(pop_size):
    return [generate_individual() for _ in range(pop_size)]

# Sélection des individus pour la reproduction (tournoi binaire)
def selection(population):
    tournament_size = 3
    selected = []
    for _ in range(len(population)):
        candidates = random.sample(population, tournament_size)
        winner = min(candidates, key=evaluate_individual)
        selected.append(winner)
    return selected

# Croisement (recombinaison)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation
def mutate(individual, mutation_rate):
    mutated_individual = []
    for gene in individual:
        if random.random() < mutation_rate:
            mutated_individual.append(gene + random.uniform(-0.5, 0.5))
        else:
            mutated_individual.append(gene)
    return mutated_individual

# Algorithme génétique
def genetic_algorithm(population_size, num_generations):
    mutation_rate = 0.1
    population = generate_population(population_size)

    for generation in range(num_generations):
        population = sorted(population, key=evaluate_individual)
        parents = selection(population)

        next_generation = []

        for _ in range(population_size // 2):
            parent1, parent2 = random.sample(parents, 2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])

        population = next_generation

    best_individual = min(population, key=evaluate_individual)
    return best_individual

# Exemple d'utilisation
best_solution = genetic_algorithm(population_size=100, num_generations=100)
print("Meilleure solution trouvée:", best_solution)
print("Distance à l'objectif:", evaluate_individual(best_solution))


#
# listDonnes = (transObjectList(listVilles))
# print(listDonnes)
# folium.PolyLine(locations=genetic_algorithm(listDonnes, 100), color ='blue').add_to(mapp)
# mapp.save("index.html")