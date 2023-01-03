<h1>DNS Cache Manager</h1>

This script allows you to manage the Domain Name System (DNS) cache on your device. You can clear the cache, add custom entries to the cache, or display the current contents of the cache.

<h4>Features</h4>

    Clear the DNS cache on Windows or macOS.
    Add custom DNS entries to the cache on Windows or macOS.
    Display the current contents of the DNS cache on Windows or macOS.

<h4>Requirements</h4>

    Python 3
    The os and time modules (included in the Python standard library)

<h4>Usage</h4>

    Run the script.
    Select one of the following options:
        Clear DNS cache
        Add custom DNS entry
        Show DNS cache
        Quit
    Follow the prompts to complete the selected task.

<h4>Notes</h4>

    On Windows, the script uses the ipconfig command to clear the cache and display its contents. On macOS, it uses the dscacheutil and scutil commands.
    On macOS, the script requires sudo privileges to add a custom DNS entry. You will be prompted to enter your password.
    The script will run indefinitely until you select the "Quit" option. To exit the script, press CTRL + C on the command line.
