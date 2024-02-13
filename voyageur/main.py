from tkinter import filedialog

import folium
import csv


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


# def selectionsort(Ville):
#     def swap(idxi, idxj):
#         temp = (
#             Ville)[idxi]
#
#         Ville[idxi] = (
#             Ville)[idxj]
#
#         Ville[idxj] = temp
#
#     nb = len(
#         Ville)
#     for i in range(0, nb):
#         min = i
#         for j in range(i + 1, nb):
#             if (
#                     Ville[j].distance <
#                     Ville[min].distance):
#                 min = j
#         swap(i, min)
#
#     return (Ville)



def getDistance(ville):
    R = 6373.0

    lat1 = radians(45.166672)
    lon1 = radians(5.71667)
    lat2 = radians(m.latitude)
    lon2 = radians(m.longitude)

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

def transObjetList(listVilles):
    listTransph = []
    for liste in listVilles:
        listTransph.append((liste.latitude , liste.longitude))
    return listTransph

listObject=transObjetList(listVilles)
print(listObject)
folium.PolyLine(locations=listObject, color ='blue').add_to(map)

map.save("index.html")

# trail_coordinates = [
#     (45.171112, 5.695952),
#     (45.183152, 5.699386),
#     (45.174115, 5.711106),
#     (45.176123, 5.722083),
#     (45.184301, 5.719791),
#     (45.184252, 5.730698),
#     (45.170588, 5.716664),
#     (45.193702, 5.691028),
#     (45.165641, 5.739938),
#     (45.178718, 5.744940),
#     (45.176857, 5.762518),
#     (45.188512, 5.767172),
# ]
#
# folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)

#
#
#
# folium.Map(tiles='https://{s}.tiles.example.com/{z}/{x}/{y}.png', attr='My Data Attribution')





# def 2-opt (m):
#     for Ville_1 in range (1, n) :
#         for Ville_2 in range (1 + 1 , n):
#             if Ville_1 - Ville_2 < 0 :
#                 Ville_1 , Ville_2 = Ville_2, Ville_1



# def reverse_subtour(path, i, j):
#     while i < j:
#         path[i % len(path)], path[j % len(path)] = path[j % len(path)], path[i % len(path)]
#         i += 1
#         j -= 1
#
# def calculate_gain(path, i, j):
#     N = len(path)
#     gain = 0
#     if i + 1 < j - 1:
#         gain = (
#             distance(path[(i+N-1) % N], path[j % N]) +
#             distance(path[j % N], path[(i+N+1) % N]) +
#             distance(path[(j+N-1) % N], path[i % N]) +
#             distance(path[i % N], path[(j+N+1) % N]) -
#             distance(path[(i+N-1) % N], path[i % N]) -
#             distance(path[i % N], path[(i+N+1) % N]) -
#             distance(path[(j+N-1) % N], path[j % N]) -
#             distance(path[j % N], path[(j+N+1) % N])
#         )
#     return gain
#
# def optimize_path(path):
#     N = len(path)
#     improved = True
#     while improved:
#         improved = False
#         for i in range(N):
#             for j in range(i + 1, N):
#                 reverse_subtour(path, i, j)
#                 gain = calculate_gain(path, i, j)
#                 if gain < 0:
#                     reverse_subtour(path, i, j)  # Revert the reversal
#                 else:
#                     improved = True
#     return path
#
# optimize_path(m)
