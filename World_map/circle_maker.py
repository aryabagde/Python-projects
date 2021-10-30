import folium
import pandas

def height_color(el):
    if el<1000:
        return"green"
    elif el>1000 and el<2000:
        return "orange"
    else:
        return "red"

data=pandas.read_csv("Volcanoes.txt")
la=list(data["LAT"])
lo=list(data["LON"])
el=list(data["ELEV"])

map=folium.Map(location=[70,90],zoom_start=6,tiles="Stamen Terrain")

fg=folium.FeatureGroup(name="My Map")

for latitude,longitude,elevation in zip(la,lo,el):
     fg.add_child(folium.CircleMarker(location=[latitude,longitude],radius=7,popup=("Height of volcano is:\n"+str(elevation)+
                  "m"),fill_color="height_color(elevation)",color="grey",fill_opacity=0.7,fill=True))

map.add_child(fg)
map.save("Map2.html")
