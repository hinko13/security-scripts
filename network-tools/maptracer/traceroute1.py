import folium
import subprocess

def traceroute(destination, max_hops=None, packet_size=None):
  cmd = ["traceroute"]
  if max_hops is not None:
    cmd.extend(["-m", str(max_hops)])
  if packet_size is not None:
    cmd.extend(["-s", str(packet_size)])
    cmd.append(destination)
      
#Run traceroute
return subprocess.check_output(cmd)

def main():
#user input
input_method = input("Enter 's' for a specific destination or 'l' for a list/CSV file: ")

if input_method == 's':
    # Get destination 
    destination = input("Enter destination: ")
    # Perform traceroute
    output = traceroute(destination)
    print(output.decode())
elif input_method == 'l':
    # Get file path from user
    file_path = input("Enter file path: ")
    # Open file
    with open(file_path, 'r') as file:
        # Read each line in file
        for line in file:
            # Strip leading/trailing whitespace and perform traceroute
            output = traceroute(line.strip())
            print(output.decode())
else:
    print("Invalid input method")

if name == "main":
main()
