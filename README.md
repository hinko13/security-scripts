# security-scripts


##website-security
This directory contains a collection of scripts that can be used to check the security of websites.

###processing_and_printing_csv_data.py 
This script reads a CSV file and stores each row in a list. It then processes and prints a sublist of the list, as well as commented out code to process and print a different list.

###ssl_certificate_authority_lookup.py 
This script creates an SSL (Secure Sockets Layer) context and wraps a socket object with it. It then connects to the specified hostname on port 443 (the default port for HTTPS connections) and retrieves the certificate of the server it connects to. It then extracts the subject and issuer of the certificate and prints the common name of the issuer.

###ssl_certificate_issuer.py 
This script imports a list of hostnames from a CSV file and attempts to retrieve the SSL certificate for each hostname. It then writes the hostname and the issuer of the certificate to an output file, or a message indicating that the certificate information could not be obtained if an error occurs.

