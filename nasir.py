import folium

# Create base map centered on the region
m = folium.Map(location=[36.5, 62.0], zoom_start=6)

# Define coordinates in order of visit
coordinates = [
    [37.6639, 62.1904, "Merv"],
    [35.6383, 63.2845, "Marv Rud"],
    [36.7500, 65.7500, "Jowzjan"],
    [36.6676, 65.7529, "Shaburghan"],
    [36.3150, 68.0239, "Samangan"],
    [36.7333, 69.5333, "Taleqan"],
    [36.2130, 58.7949, "Nishapur"],
    [36.5449, 61.1577, "Sarakhs"],
    [36.1680, 54.3480, "Damghan"],
    [35.5769, 53.3992, "Semnan"]
]

# Add markers and connect with lines
for coord in coordinates:
    folium.Marker(
        [coord[0], coord[1]],
        popup=coord[2],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

# Create line connecting points in order
folium.PolyLine(
    locations=[[c[0], c[1]] for c in coordinates],
    weight=2,
    color='blue',
    opacity=0.8,
    popup='Nasir Khusraw\'s Route'
).add_to(m)

# Add title and legend
title_html = '''
             <h3 align="center" style="font-size:16px">
             <b>Nasir Khusraw's Journey Route (437 AH/1046 CE)</b>
             </h3>
             '''
m.get_root().html.add_child(folium.Element(title_html))

m.save('khusraw_route.html')
