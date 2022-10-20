from ast import arg
import folium
import pandas


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(el):
    if el < 1000:
        return "green"
    elif 1000<= el and el <3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[10.7, 106.6], zoom_start=20, tiles="Stamen Terrain")


# %22 replace for the double quotes " when URL encoding to search
html = """
<strong>Volcano name:</strong><br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, nam in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html % (nam, nam, el), width=180, height=60)
    # fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=7,popup=folium.Popup(iframe), fill_color=color_producer(el), 
                                     color="grey", fill_opacity=0.7))
# for coordinate in [[10.7, 106.6],[15.7, 106.6]]:
#     fg.add_child(folium.Marker(location=coordinate, popup="Hi, This is a MARKER", icon=folium.Icon(color="green")))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
            style_function= (lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 
                                      else 'orange' if (x['properties']['POP2005'] >=10000000 and x['properties']['POP2005'] <20000000) 
                                      else 'red'})))                       

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("webMap.html")