import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lt=list(data["LAT"])
ln=list(data["LON"])
el=list(data["ELEV"])

def height(el):
        if el<1000:
            return "green"
        elif el>1000 and el<3000:
            return "orange"
        else:
            return "red"

map=folium.Map(loaction=[19.803,70.805],zoom_start=6,tiles="Stamen Terrain")#whenever you want to call a function from imported module type <module>.<function>(<parameters>)

fga=folium.FeatureGroup(name="Volcanoes")#Should make feature groups so that u can add more features in a single map.

for latitude,longitude,elevation in zip(lt,ln,el):
    fga.add_child(folium.Marker(location=[latitude,longitude],popup=("Hieght of volcano is:\n"+str(elevation)+"m"),icon=folium.Icon(color=height(elevation))))#folium.marker is a feature.
fgb=folium.FeatureGroup(name="Population")
fgb.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
               style_function= lambda x:{"fillColor":"green" if x['properties']['POP2005']<10000000
               else 'orange'if 10000000<= x['properties']['POP2005']<20000000 else 'red'} ))#adding polygons is the second feature

map.add_child(fga)
map.add_child(fgb)
map.add_child(folium.LayerControl())
map.save("Map1.html")
