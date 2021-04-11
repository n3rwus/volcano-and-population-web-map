import folium
import pandas

data = pandas.read_csv("data/Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
        if elevation < 1000:
                return "green"
        elif 1000 <= elevation < 3000:
                return "orange"
        else:
                return "red"


html =  """
        Volcano name:<br>
        <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
        Height: %s m
        """

map = folium.Map(location=[40, -102], zoom_start=5, tiles = "Stamen Terrain")

fg_v = folium.FeatureGroup(name="Volcanoes USA")

for lt, ln, el, name in zip(lat, lon, elev, name):
    
    iframe = folium.IFrame(
            html=html % (name, name, int(el)),
            width=150,
            height=80
            )
    
    fg_v.add_child(folium.CircleMarker(
            location=[lt, ln],
            radius=8,
            fill_color=color_producer(el),
            fill=True,
            fill_opacity=0.85,
            popup=folium.Popup(iframe),
            color = "grey"
            ))
    
fg_p = folium.FeatureGroup(name="Populations")
    
fg_p.add_child(folium.GeoJson(data=open("data/world.json", "r", encoding="utf-8-sig").read(),
                         style_function=lambda x:
                             {"fillColor" : "green" if x["properties"]["POP2005"] < 10000000 
                              else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000
                              else "red"}
                         ))
    
  

map.add_child(fg_p)
map.add_child(fg_v)
map.add_child(folium.LayerControl())
map.save("data/population-and-volcano-map.html")