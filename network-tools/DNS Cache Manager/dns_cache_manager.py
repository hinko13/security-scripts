import os
import time

def clear_dns_cache():
    #running Windows or macOS
    if os.name == 'nt':
        # Clear DNS on Windows
        os.system('ipconfig /flushdns')
        print("DNS cache has been cleared.")
    elif os.name == 'posix':
        # Clear DNS on macOS
        os.system('dscacheutil -flushcache')
        print("DNS cache has been cleared.")
    else:
        print("Sorry, your operating system is not supported.")

def add_dns_entry(hostname, ip_address):
    #running Windows or macOS
    if os.name == 'nt':
        # Add custom DNS entry on Windows
        os.system(f'netsh interface ip add dns name="Ethernet" addr={ip_address} {hostname}')
        print(f"{hostname} has been added to the DNS cache with the IP address {ip_address}.")
    elif os.name == 'posix':
        # Add custom DNS entry on macOS
        os.system(f'sudo bash -c "echo "{ip_address} {hostname}" >> /etc/hosts"')
        print(f"{hostname} has been added to the DNS cache with the IP address {ip_address}.")
    else:
        print("Sorry, your operating system is not supported.")

def show_dns_cache():
    #running Windows or macOS
    if os.name == 'nt':
        # Show DNS cache on Windows
        os.system('ipconfig /displaydns')
    elif os.name == 'posix':
        # Show DNS cache on macOS
        os.system('scutil --dns')
    else:
        print("Sorry, your operating system is not supported.")

while True:
    print("1. Clear DNS cache")
    print("2. Add custom DNS entry")
    print("3. Show DNS cache")
    print("4. Quit")


    # user input
    selection = input("Enter your selection: ")

    # Clear DNS cache
    if selection == '1':
        clear_dns_cache()
    # Add custom DNS entry
    elif selection == '2':
        hostname = input("Enter hostname: ")
        ip_address = input("Enter IP address: ")
        add_dns_entry(hostname, ip_address)
    # Show DNS cache
    elif selection == '3':
        show_dns_cache()
    # Quit
    elif selection == '4':
        break
    # Invalid selection
    else:
        print("Invalid selection. Please try again.")

#prevent spamming commands
time.sleep(1)
