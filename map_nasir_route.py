import folium
from geopy.geocoders import Nominatim

def create_caravan_route_map():
    # Initialize map centered around the region
    m = folium.Map(location=[36.5, 62.0], zoom_start=6)
    
    # Key locations with waypoints following historical caravan paths
    route_points = [
        ("Merv", 37.6639, 61.8267),
        ("Caravan Stop 1", 37.2000, 61.5000),
        ("Sarakhs", 36.5449, 61.1577),
        ("Caravan Stop 2", 36.4000, 60.2000),
        ("Nishapur", 36.2132, 58.7958),
        ("Caravan Stop 3", 36.3000, 62.5000),
        ("Faryab", 36.0797, 64.9070),
        ("Shaburghan", 36.6676, 65.7529),
        ("Caravan Stop 4", 36.5000, 66.8000),
        ("Samangan", 36.3153, 68.0049),
        ("Taleqan", 36.7360, 69.5345),
        ("Marw al-Rudh", 35.7481, 63.9043),
        ("Caravan Stop 5", 35.9000, 59.2000),
        ("Damghan", 36.1680, 54.3480),
        ("Semnan", 35.5769, 53.3992)
    ]
    
    # Add markers for main cities
    for name, lat, lon in route_points:
        if "Caravan Stop" not in name:
            folium.Marker(
                [lat, lon],
                popup=name,
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)
    
    # Create route line following terrain
    points = [[lat, lon] for _, lat, lon in route_points]
    folium.PolyLine(
        points, 
        weight=3, 
        color='brown', 
        opacity=0.8,
        tooltip="Historical Caravan Route"
    ).add_to(m)
    
    # Add terrain layer with attribution
    folium.TileLayer(
        tiles='Stamen Terrain',
        attr='Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.',
        name='Terrain View'
    ).add_to(m)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    
    # Save map
    m.save('nasir_khusraw_caravan_route.html')

if __name__ == "__main__":
    create_caravan_route_map()
