import folium
import subprocess
from urllib.parse import urlparse
import geoip2.database

class Coordinates:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        
def get_traceroute_route(destination):
    # Parse the URL to extract the domain name
    domain_name = urlparse(destination).netloc
    # Run tracert command and get output
    output = subprocess.check_output(["tracert", "-d", destination]).decode()
    # Split output into lines
    lines = output.split("\n")
    # Initialize list to store hop locations
    locations = []
    # Iterate over lines
    for line in lines:
        # Split line into fields
        fields = line.split()
        # Check if line contains hop information
        if len(fields) >= 3 and fields[1].isdigit():
            # Extract hop location and clean things up
            location = fields[2]
            location = location.strip("[]")
            # print(fields)
            # fields example: ['1', '3', 'ms', '2', 'ms', '5', 'ms', '192.168.0.1']
            # Reader object.
            # use limited, creation is expensive.
            ip_address = fields[7]
            try:
                with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
                    response = reader.city(ip_address)
                    coordinates = Coordinates(latitude=response.location.latitude,longitude=response.location.longitude)
                    if coordinates is not None:
                        locations.append((coordinates.latitude, coordinates.longitude))
            except Exception as e:
                print(f"Error resolving coordinates for {ip_address}: {e}")
    return locations


    
def create_map(destination, route):
#does route exist
    if not route:
        print("No route found")
        return
    # Create map centered on the first hop in the route
    map = folium.Map(location=route[0], zoom_start=3)
    # Add markers for each hop in the route
    for location in route:
        folium.Marker(location=location).add_to(map)
    # Add a line connecting the markers
    folium.PolyLine(route, color="red", weight=2.5, opacity=1).add_to(map)
    # Add a title to the map
    folium.map.Marker(
        [0, 0], 
        icon=None, 
        popup=f"<b>Traceroute to {destination}</b>"
    ).add_to(map)
    # Display map
    map.save(f"{destination}.html")

# Prompt user for input method
input_method = input("Enter 's' for a specific destination or 'l' for a list/CSV file: ")

if input_method == 's':
    # Get destination from user
    destination = input("Enter destination: ")
    # Get traceroute route to destination
    route = get_traceroute_route(destination)
    # Create map of traceroute route
    create_map(destination, route)
elif input_method == 'l':
    # Get file path from user
    file_path = input("Enter file path: ")
    # Open file
    with open(file_path, 'r') as file:
        # Read each line in file
        for line in file:
            # Strip leading/trailing whitespace and perform traceroute
            get_traceroute_route(line.strip())(line.strip())
else:
    print("Invalid input method")
