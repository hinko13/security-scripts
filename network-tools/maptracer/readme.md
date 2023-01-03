<h1>Map Tracer</h1>

A Python script that uses the traceroute command to trace the route taken to reach a given destination, and visualizes the route on a map using the Folium library.

<h3>Requirements</h3>

    Python 3.6+
    Folium 0.11.0+
    geoip2 2.10.0+

<h3>Usage</h3>

    Run the script using python map_tracer.py
    Choose to enter a specific destination or a list/CSV file of destinations
    For a specific destination, enter the URL or domain name
    For a list/CSV file, enter the file path
    A map will be generated and saved as an HTML file in the same directory as the script

<h3>Example</h3>

<h5>Input:</h5>

    python map_tracer.py
    Enter 's' for a specific destination or 'l' for a list/CSV file: s
    Enter destination: google.com


<h5>Output:</h5>

<h3>Example Map</h3>

![image](https://user-images.githubusercontent.com/621718/210338332-c798e03b-2633-477c-9eb6-8686226151de.png)
