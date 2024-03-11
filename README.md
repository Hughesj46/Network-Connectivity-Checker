# Network-Connectivity-Checker
This Python script is created to check the connection of a list of IP addresses. It utilizes socket connections to determine whether a given IP address is reachable or not.
How to Use
Requirements: Ensure you have Python installed on your system. This script is compatible with both Python 2 and Python 3.
Clone the Repository: If you're using this script from a repository, clone or download the repository to your local machine.
Run the Script: Open a terminal or command prompt, navigate to the directory containing the script, and run it by executing the command: python connectivity_checker.py.
Input IP Addresses: Upon running the script, you'll be prompted to enter the IP addresses you wish to check. Enter the IP addresses separated by commas and press Enter.
View Results: The script will then proceed to check the connectivity of each entered IP address. It will output whether each IP address is reachable or unreachable.
Notes
Timeout: The script has a timeout of 5 seconds for each connection attempt. You can modify this timeout value in the check_connectivity and is_device_connectable functions if needed.
Error Handling: The script handles errors such as invalid IP addresses and connection timeouts gracefully, ensuring smooth execution.
IPv6 Support: The script supports both IPv4 and IPv6 addresses.
Input Format: Ensure the input IP addresses are in a valid format (IPv4 or IPv6) separated by commas.

