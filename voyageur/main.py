import folium
import csv


# class Ville :
#     def __init__(self, latitude , longitude):
#         self.latitude = latitude
#         self.longitude = longitude


m = folium.Map([45.171112, 5.695952], zoom_start=12)


folium.Marker(
    location=[45.183152, 5.699386],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=[45.174115, 5.711106],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)
folium.Marker(
    location=[45.171112, 5.695952],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)


folium.Marker(
    location=[45.176123, 5.722083],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=[45.184301, 5.719791],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=[45.184252, 5.730698],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=[45.170588, 5.716664],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=[45.193702, 5.691028],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=[45.165641, 5.739938],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=[45.178718, 5.744940],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=[45.176857, 5.762518],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=[45.188512, 5.767172],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="red"),
).add_to(m)

trail_coordinates = [
    (45.171112, 5.695952),
    (45.183152, 5.699386),
    (45.174115, 5.711106),
    (45.176123, 5.722083),
    (45.184301, 5.719791),
    (45.184252, 5.730698),
    (45.170588, 5.716664),
    (45.193702, 5.691028),
    (45.165641, 5.739938),
    (45.178718, 5.744940),
    (45.176857, 5.762518),
    (45.188512, 5.767172),
]

folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)



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