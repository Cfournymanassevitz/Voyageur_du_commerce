from tkinter import filedialog

import folium
import csv
from math import radians, sin, cos, atan2, sqrt


class Ville :
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


listVilles = []
def loadFile():

    with open('../villes/ville.csv', 'r', encoding='UTF-8') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            data = row[0].split(";")

            ville = Ville(float(data[0]), float(data[1]))
            listVilles.append(ville)




loadFile()
print(listVilles)


def getDistance(ville1, ville2):
    R = 6373.0

    lat1 = radians(ville1[0])
    lon1 = radians(ville1[1])
    lat2 = radians(ville2[0])
    lon2 = radians(ville2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance

map = folium.Map([45.171112, 5.695952], zoom_start=12)

for i in range(len(listVilles)):
    folium.Marker(
        location=[listVilles[i].latitude,listVilles[i].longitude],
        popup="Timberline Lodge",
        icon=folium.Icon(color="blue"),).add_to(map)



def distance(lat1, lon1, lat2, lon2):
    R = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance

def distance_total(listDonnes):

    distance_to = 0
    for i in range(0, len(listDonnes)-1):
        avance = i +1
        #calculer distance entre i et avancer recupéré ville i et ville +1
        ville1 = listDonnes[i]
        ville2 = listDonnes[avance]
        distance_actuel= distance(ville1[0], ville1[1], ville2[0], ville2[1])
        #ajouter cette distance a la ditance total
        distance_to += distance_actuel
    return distance_to



def glouton(listDonnes):
    solution = listDonnes[0:2]
    full = len(listDonnes)
    site_non_selectionne = listDonnes[3:full]

    while len(solution) < full and len(site_non_selectionne) != 0:
        prochaine_ville = site_non_selectionne.pop(0)
        # récupérer mini combinaison
        plus_petite_combi= get_petite_cobinaison(solution,prochaine_ville)
        # remplacer le chemin par min combinaison
        solution = plus_petite_combi

    return solution

def get_petite_cobinaison(solution,prochaine_ville):
    solution_optimal = []
    distance_optimal= float('inf')
#boucle parcour solution ou on test prochaine ville dans solution
    taille_solution = len(solution)
    for i in range(0,taille_solution):
        solution.insert(i,prochaine_ville)
        distance_total(solution)
        if distance_total(solution) < distance_optimal:
            distance_optimal = distance_total(solution)
            solution_optimal = solution[:]
        solution.pop(i)
    return solution_optimal

#place prochaine ville et on calcule la total distance
#comparer nouvelle total distance avec ancienne et remplacer si plus petit
#pop la ville que on vien de placer pour la supprimer
# return la combinaiseon la plus petite
def transObjectList(listVilles):
    listTrans = []
    for liste in listVilles:
        listTrans.append((liste.latitude , liste.longitude))
    return listTrans


listDonnes = (transObjectList(listVilles))
print(listDonnes)
folium.PolyLine(locations=glouton(listDonnes), color ='blue').add_to(map)
map.save("index.html")

print(glouton(listDonnes))

print(distance_total(listDonnes))





