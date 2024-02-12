from tkinter import filedialog

import folium
import csv


class Ville :
    def __init__(self, latitude , longitude,distance):
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance



def loadFile():
    Ville.clear()
    filename = filedialog.askopenfilename(initialdir="./",
                                          title="Selection du Fichier",
                                          filetypes=(("Text files",
                                                      "*.csv*"),
                                                     ("all files",
                                                      "*.*")))
    changeLabelFile("Fichier : "+filename)
    with open(filename, 'r', encoding='UTF-8') as file:
        csvreader = csv.reader(file)
        next(csvreader)  # skip header line
        for row in csvreader:
            data = row[0].split(";")
            try:
                ville = Ville(data[8], data[9], float(data[11]), float(data[12]), float(data[13]), 0)
                ville.distance = getDistance(ville)
                Ville.append(ville)
            except:
                continue

def selectionsort(
        Ville):
    def swap(idxi, idxj):
        temp = (
            Ville)[idxi]

        Ville[idxi] = (
            Ville)[idxj]

        Ville[idxj] = temp

    nb = len(
        Ville)
    for i in range(0, nb):
        min = i
        for j in range(i + 1, nb):
            if (
                    Ville[j].distance <
                    Ville[min].distance):
                min = j
        swap(i, min)

    return (
        Ville)

    return (
        Ville)

def getDistance(ville):
    R = 6373.0

    lat1 = radians(45.166672)
    lon1 = radians(5.71667)
    lat2 = radians(ville.latitude)
    lon2 = radians(ville.longitude)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance

m = folium.Map([45.171112, 5.695952], zoom_start=12)

#
# folium.Marker(
#     location=[45.183152, 5.699386],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
#
# folium.Marker(
#     location=[45.174115, 5.711106],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
# folium.Marker(
#     location=[45.171112, 5.695952],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
#
#
# folium.Marker(
#     location=[45.176123, 5.722083],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
#
# folium.Marker(
#     location=[45.184301, 5.719791],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
#
# folium.Marker(
#     location=[45.184252, 5.730698],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
#
# folium.Marker(
#     location=[45.170588, 5.716664],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
#
# folium.Marker(
#     location=[45.193702, 5.691028],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
#
# folium.Marker(
#     location=[45.165641, 5.739938],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
#
# folium.Marker(
#     location=[45.178718, 5.744940],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
#
# folium.Marker(
#     location=[45.176857, 5.762518],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
#
# folium.Marker(
#     location=[45.188512, 5.767172],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="red"),
# ).add_to(m)
#
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




# def loadFile() :

# m = folium.Map(location=(45.171112, 5.695952))
# folium.Map(tiles='https://{s}.tiles.example.com/{z}/{x}/{y}.png', attr='My Data Attribution')

#
# folium.Marker(
#     location=[45.3288, -121.6625],
#     tooltip="Click me!",
#     popup="Mt. Hood Meadows",
#     icon=folium.Icon(icon="cloud"),
#
# ).add_to(m)
#
# folium.Marker(
#     location=[45.3311, -121.7113],
#     tooltip="Click me!",
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="green"),
# ).add_to(m)
#
# m
# m = folium.Map(location=[-71.38, -73.9], zoom_start=11)
#
#
# folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)
#
# m
m.save("index.html")