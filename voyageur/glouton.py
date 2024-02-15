import math
from tkinter import filedialog

import folium
import csv
from math import radians, sin, cos, atan2, sqrt
from haversine import haversine


class Ville :
    def __init__(self, latitude, longitude, index):
        self.latitude = latitude
        self.longitude = longitude
        self.index = index


listVilles = []
def loadFile():

    with open('../villes/ville.csv', 'r', encoding='UTF-8') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for index, row in enumerate(csvreader):
            data = row[0].split(";")

            ville = Ville(float(data[0]), float(data[1]), index)
            listVilles.append(ville)




loadFile()
print(listVilles)
listVilles = listVilles


# def getDistance(city1, city2):
#     phi1 = city1.longitude * math.pi/180
#     phi2 = city2.longitude * math.pi/180
#     delta_lon = (city2.latitude - city1.latitude) * math.pi/180
#     R = 6371e3
#     return math.acos(math.sin(phi1)*math.sin(phi2) + math.cos(phi1)*math.cos(phi2) * math.cos(delta_lon)) * R




def distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))

    # Radius of earth in kilometers is 6371
    km = 6371 * c
    return km

mapp = folium.Map([45.171112, 5.695952], zoom_start=12)

for i in range(len(listVilles)):
    folium.Marker(
        location=[listVilles[i].latitude,listVilles[i].longitude],
        popup=i,
        icon=folium.Icon(color="blue"),).add_to(mapp)

def distance_total(listDonnes):
    # villeDebut = listDonnes[0]
    # villeFin = listDonnes[-1]
    # # distance_fin = distance(villeDebut[0], villeDebut[1], villeFin[0], villeFin[1])
    distance_to = 0
    for i in range(0, len(listDonnes)-1):
        avance = i +1
        #calculer distance entre i et avancer recupéré ville i et ville +1
        ville1 = listDonnes[i]
        ville2 = listDonnes[avance]
        distance_actuel= distance(ville1[0], ville1[1], ville2[0], ville2[1])
        #ajouter cette distance a la ditance total
        distance_to += distance_actuel
    distance_to += distance(listDonnes[0][0], listDonnes[0][1],listDonnes[-1][0],listDonnes[-1][1])
    return distance_to



def glouton(listDonnes):
    solution = listDonnes[0:3]
    full = len(listDonnes)
    site_non_selectionne = listDonnes[3:full]

    while len(solution) < full and len(site_non_selectionne) != 0:
        prochaine_ville = site_non_selectionne.pop(0)
        # récupérer mini combinaison
        plus_petite_combi= get_petite_cobinaison(solution,prochaine_ville)
        # remplacer le chemin par min combinaison
        solution = plus_petite_combi
    solution.append(solution[0])
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
folium.PolyLine(locations=glouton(listDonnes), color ='blue').add_to(mapp)
mapp.save("index.html")

# print()

print(distance_total(glouton(listDonnes)[0:len(listDonnes)-1]))


# print(distance(listVilles[0].latitude,listVilles[0].longitude,listVilles[24].latitude,listVilles[24].longitude))


