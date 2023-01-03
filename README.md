# security-scripts

<h2>network-tools</h2>
The network-tools directory contains a few different scripts that can be used to perform various network diagnostic and testing tasks.


<h3>Map Tracer</h3>
This is a python script that uses the traceroute command to trace the route taken to reach a given destination, and visualizes the route on a map using the Folium library.

<h3>icmp_echo_request_and_reply_parser.py</h3>
This script runs the ping command with certain arguments to send a specified number of ICMP (Internet Control Message Protocol) echo request packets to a specified IP address and waits for the corresponding echo reply packets. It then parses the output of the ping command to extract the packet loss, minimum, average, and maximum round trip times for the packets.

<h3>ping_testing_script.py</h3> 
This script runs the ping command with certain arguments to send a specified number of ICMP echo request packets to a specified IP address and waits for the corresponding echo reply packets. It then checks the response of the ping command and prints the results.


<h2>website-security</h2>
The website-security directory contains a collection of scripts that can be used to check the security of websites.

<h3>processing_and_printing_csv_data.py</h3>
This script reads a CSV file and stores each row in a list. It then processes and prints a sublist of the list, as well as commented out code to process and print a different list.

<h3>ssl_certificate_authority_lookup.py</h3> 
This script creates an SSL (Secure Sockets Layer) context and wraps a socket object with it. It then connects to the specified hostname on port 443 (the default port for HTTPS connections) and retrieves the certificate of the server it connects to. It then extracts the subject and issuer of the certificate and prints the common name of the issuer.

  <h3>ssl_certificate_issuer.py</h3> 
This script imports a list of hostnames from a CSV file and attempts to retrieve the SSL certificate for each hostname. It then writes the hostname and the issuer of the certificate to an output file, or a message indicating that the certificate information could not be obtained if an error occurs.

